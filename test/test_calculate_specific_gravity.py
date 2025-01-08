import unittest
from specific_gravity_calculator import calculate_specific_gravity,
  # Replace 'your_module_name' with the actual module name
class TestTestCalculateSpecificGravity(unittest.TestCase):
    def test_valid_input(self):
        """Test with valid inputs."""
        self.assertAlmostEqual(calculate_specific_gravity(4, 2), 2.0)
        self.assertAlmostEqual(calculate_specific_gravity(5, 2), 1.6666666666666667)

    def test_equal_weights(self):
        """Test when weight in air is equal to weight in water."""
        self.assertIsNone(calculate_specific_gravity(2, 2))

    def test_weight_in_air_less_than_water(self):
        """Test when weight in air is less than weight in water."""
        self.assertIsNone(calculate_specific_gravity(1, 2))

    def test_invalid_inputs(self):
        """Test with invalid inputs like negative values."""
        self.assertIsNone(calculate_specific_gravity(-4, 2))
        self.assertIsNone(calculate_specific_gravity(4, -2))
        self.assertIsNone(calculate_specific_gravity(-4, -2))


if __name__ == "__main__":
    unittest.main()
