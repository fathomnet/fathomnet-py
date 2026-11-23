import warnings
from unittest import TestCase

from fathomnet import dto
from fathomnet.api import _paging, boundingboxes, geoimages
from fathomnet.util import page


def fake_page_fn(total: int, calls: list = None, default_size: int = 1000):
    """Make a page function over the items 0..total-1 that records the pageables it is called with."""
    items = list(range(total))

    def page_fn(pageable):
        if calls is not None:
            calls.append(pageable)
        size = (pageable.size if pageable else None) or default_size
        size = min(size, _paging.MAX_PAGE_SIZE)
        number = (pageable.number if pageable else None) or 0
        content = items[number * size : (number + 1) * size]
        return dto.Page[int](
            content=content,
            pageNumber=number,
            pageSize=size,
            totalPages=-(-total // size),
            totalItems=total,
        )

    return page_fn


class TestPageDTO(TestCase):
    def test_from_dict(self):
        p = dto.Page[dto.GeoImage].from_dict(
            {
                "content": [{"uuid": "a"}],
                "pageNumber": 0,
                "pageSize": 1,
                "totalPages": 2,
                "totalItems": 2,
            }
        )
        self.assertIsInstance(p.content[0], dto.GeoImage)
        self.assertEqual(p.totalItems, 2)
        self.assertFalse(p.is_last)

    def test_from_bare_list(self):
        p = dto.Page[str].from_dict(["a", "b"])
        self.assertEqual(p.content, ["a", "b"])
        self.assertEqual(p.totalItems, 2)
        self.assertTrue(p.is_last)


class TestPageable(TestCase):
    def test_to_params_with_sort_direction(self):
        pageable = dto.Pageable.from_params(
            size=5, page=2, sort_keys=["displayName,desc", "uuid"]
        )
        self.assertEqual(
            pageable.to_params(),
            [("size", 5), ("page", 2), ("sort", "displayName,DESC"), ("sort", "uuid")],
        )


class TestPagingHelpers(TestCase):
    def test_fetch_all(self):
        calls = []
        items = _paging.fetch_all(fake_page_fn(25, calls), size=10)
        self.assertEqual(items, list(range(25)))
        self.assertEqual(len(calls), 3)

    def test_fetch_all_empty(self):
        self.assertEqual(_paging.fetch_all(fake_page_fn(0), size=10), [])

    def test_fetch_range_aligned(self):
        calls = []
        items = _paging.fetch_range(fake_page_fn(100, calls), limit=10, offset=20)
        self.assertEqual(items, list(range(20, 30)))
        self.assertEqual(len(calls), 1)

    def test_fetch_range_unaligned(self):
        items = _paging.fetch_range(fake_page_fn(100), limit=10, offset=25)
        self.assertEqual(items, list(range(25, 35)))

    def test_fetch_range_past_end(self):
        self.assertEqual(
            _paging.fetch_range(fake_page_fn(30), limit=10, offset=25),
            list(range(25, 30)),
        )
        self.assertEqual(_paging.fetch_range(fake_page_fn(30), limit=10, offset=40), [])

    def test_fetch_range_over_max_page_size(self):
        limit = _paging.MAX_PAGE_SIZE + 5
        items = _paging.fetch_range(fake_page_fn(limit + 100), limit=limit, offset=3)
        self.assertEqual(items, list(range(3, 3 + limit)))

    def test_fetch_range_zero_limit(self):
        self.assertEqual(_paging.fetch_range(fake_page_fn(10), limit=0, offset=0), [])

    def test_list_result_limit_offset_is_deprecated(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            items = _paging.list_result(fake_page_fn(100), limit=5, offset=7)
        self.assertEqual(items, list(range(7, 12)))
        self.assertTrue(any(issubclass(x.category, DeprecationWarning) for x in w))

    def test_list_result_rejects_both(self):
        with self.assertRaises(ValueError):
            _paging.list_result(fake_page_fn(10), dto.Pageable(size=2), limit=2)

    def test_list_result_modes(self):
        fn = fake_page_fn(2500)
        self.assertEqual(len(_paging.list_result(fn)), 1000)  # server default page
        self.assertEqual(len(_paging.list_result(fn, all_pages=True)), 2500)
        self.assertEqual(
            _paging.list_result(fn, dto.Pageable(size=3, number=1)), [3, 4, 5]
        )


class TestUtilPage(TestCase):
    def test_page_with_page_results(self):
        calls = []
        fn = fake_page_fn(25, calls)
        self.assertEqual(list(page(fn, 10)), list(range(25)))
        self.assertEqual(len(calls), 3)  # stops on the last page without an extra request

    def test_page_with_list_results(self):
        fn = fake_page_fn(25)
        self.assertEqual(list(page(lambda p: fn(p).content, 10)), list(range(25)))


class TestPagedEndpoints(TestCase):
    def test_geoimages_find_page(self):
        constraints = dto.GeoImageConstraints(
            concept="Bathochordaeus", pageSize=3, pageNumber=1
        )
        result = geoimages.find_page(constraints)
        self.assertEqual(result.pageNumber, 1)
        self.assertEqual(len(result.content), 3)
        self.assertGreater(result.totalItems, 3)

    def test_geoimages_find_matches_page(self):
        constraints = dto.GeoImageConstraints(
            concept="Bathochordaeus", pageSize=3, pageNumber=1
        )
        self.assertEqual(
            [g.uuid for g in geoimages.find(constraints)],
            [g.uuid for g in geoimages.find_page(constraints).content],
        )

    def test_boundingboxes_find_page(self):
        constraints = dto.BoundingBoxConstraintsDTO(
            concept="Bathochordaeus", pageSize=2, pageNumber=0
        )
        result = boundingboxes.find_page(constraints)
        self.assertEqual(len(result.content), 2)
        self.assertGreater(result.totalItems, 2)

    def test_find_concepts_page(self):
        result = boundingboxes.find_concepts_page(dto.Pageable(size=3))
        self.assertGreater(len(result.content), 0)
        self.assertIsNotNone(result.totalItems)

    def test_find_concepts_is_complete(self):
        total = boundingboxes.find_concepts_page(dto.Pageable(size=1)).totalItems
        self.assertEqual(len(boundingboxes.find_concepts()), total)
