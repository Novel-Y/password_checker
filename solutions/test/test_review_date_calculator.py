#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from solutions.review_date_calculator import calculate_review_days


class TestCalculateReviewDays(unittest.TestCase):
    """Unit tests for the calculate_review_days function."""

    def test_start_day_1(self):
        """Test case for start day 1."""
        self.assertEqual(calculate_review_days(1), [2, 4, 8, 16])

    def test_start_day_15(self):
        """Test case for start day 15."""
        self.assertEqual(calculate_review_days(15), [16, 18, 22, 30])

    def test_start_day_30(self):
        """Test case for start day 30."""
        self.assertEqual(calculate_review_days(30), [31, 2, 6, 14])

    def test_start_day_31(self):
        """Test case for start day 31."""
        self.assertEqual(calculate_review_days(31), [1, 3, 7, 15])

    def test_start_day_edge(self):
        """Test case for an edge start day 28."""
        self.assertEqual(calculate_review_days(28), [29, 31, 4, 12])


if __name__ == "__main__":
    unittest.main()
