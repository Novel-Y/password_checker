#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def calculate_specific_gravity(a, w):
    """
    Calculates the specific gravity of a rock mass.

    Args:
      a: Float, weight of the rock mass measured in air.
      w: Float, weight of the rock mass measured in water.

    Returns:
      Float: The specific gravity of the rock mass.
      None: If the weight in air is less than or equal to the weight in water.

    Raises:
      ValueError: If invalid inputs are provided or the calculation cannot proceed.

    Examples:
      >>> calculate_specific_gravity(4, 2)
      2.0
      >>> calculate_specific_gravity(5, 2)
      1.6666666666666667
    """
    if a <= w:
        return None  # Return None to indicate an error
    return a / (a - w)
