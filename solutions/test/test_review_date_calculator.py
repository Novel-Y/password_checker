import unittest
from review_date_calculator import calculate_review_days


class TestCalculateReviewDays(unittest.TestCase):

    def test_start_day_1(self):
        self.assertEqual(calculate_review_days(1), [2, 4, 8, 16])

    def test_start_day_15(self):
        self.assertEqual(calculate_review_days(15), [16, 18, 22, 30])

    def test_start_day_30(self):
        self.assertEqual(calculate_review_days(30), [31, 2, 6, 14])

    def test_start_day_31(self):
        self.assertEqual(calculate_review_days(31), [1, 3, 7, 15])

    def test_start_day_edge(self):
        # Testing an edge case not covered explicitly in docstring examples
        self.assertEqual(calculate_review_days(28), [29, 31, 3, 11])


if __name__ == "__main__":
    unittest.main()
