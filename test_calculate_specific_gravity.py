"""
Unit tests for the specific_gravity_calculator module.
"""

import unittest
from calculate_specific_gravity import calculate_specific_gravity


class TestSpecificGravityCalculator(unittest.TestCase):
    """
    Test cases for the calculate_specific_gravity.
    """

    def test_equal_measurements_of_weight(self):
        """
        Test must pop 'Error: Weight in air and weight in water cannot be the same.'.
        """
        actual = calculate_specific_gravity(2,2)
        expected = 'Error: recheck your measurements.'
        self.assertTrue(actual == expected)

    def test_unequal_even_measurements_of_weight(self):
        """
        Test is being checked for unequal even measurements of weight.
        """
        actual = calculate_specific_gravity(4,2)
        expected = 2.0
        self.assertTrue(actual == expected)
        
    def test_unequal_odd_even_measurements_of_weight(self):
        """
        Test is being checked for unequal odd and even measurements of weight.
        """
        actual = calculate_specific_gravity(5,2)
        expected = 1.6666666666666667
        self.assertTrue(actual == expected)   