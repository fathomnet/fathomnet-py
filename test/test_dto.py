from unittest import TestCase

from fathomnet import dto


class TestGeoImageConstraints(TestCase):
    def test_bare_date_is_reformatted(self):
        constraints = dto.GeoImageConstraints(
            startTimestamp="2007-08-02", endTimestamp="2007-08-03"
        )
        self.assertEqual(constraints.startTimestamp, "2007-08-02T00:00:00.000Z")
        self.assertEqual(constraints.endTimestamp, "2007-08-03T00:00:00.000Z")

    def test_full_timestamp_is_unchanged(self):
        timestamp = "2007-08-02T00:00:00.000Z"
        constraints = dto.GeoImageConstraints(
            startTimestamp=timestamp, endTimestamp=timestamp
        )
        self.assertEqual(constraints.startTimestamp, timestamp)
        self.assertEqual(constraints.endTimestamp, timestamp)

    def test_offset_timestamp_is_converted_to_utc(self):
        constraints = dto.GeoImageConstraints(
            startTimestamp="2007-08-02T00:00:00-07:00"
        )
        self.assertEqual(constraints.startTimestamp, "2007-08-02T07:00:00.000Z")

    def test_naive_timestamp_is_assumed_utc(self):
        constraints = dto.GeoImageConstraints(startTimestamp="2007-08-02T12:34:56")
        self.assertEqual(constraints.startTimestamp, "2007-08-02T12:34:56.000Z")

    def test_sub_millisecond_precision_is_truncated(self):
        constraints = dto.GeoImageConstraints(
            startTimestamp="2007-08-02T00:00:00.123456Z"
        )
        self.assertEqual(constraints.startTimestamp, "2007-08-02T00:00:00.123Z")

    def test_unset_timestamps_are_none(self):
        constraints = dto.GeoImageConstraints()
        self.assertIsNone(constraints.startTimestamp)
        self.assertIsNone(constraints.endTimestamp)


class TestBoundingBoxConstraintsDTO(TestCase):
    def test_bare_date_is_reformatted(self):
        constraints = dto.BoundingBoxConstraintsDTO(
            startTimestamp="2007-08-02", endTimestamp="2007-08-03"
        )
        self.assertEqual(constraints.startTimestamp, "2007-08-02T00:00:00.000Z")
        self.assertEqual(constraints.endTimestamp, "2007-08-03T00:00:00.000Z")
