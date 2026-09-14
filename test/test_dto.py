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

    def test_unset_timestamps_are_none(self):
        constraints = dto.GeoImageConstraints()
        self.assertIsNone(constraints.startTimestamp)
        self.assertIsNone(constraints.endTimestamp)
