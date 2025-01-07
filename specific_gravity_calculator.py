#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def calculate_specific_gravity(weight_in_air, weight_in_water):
  """
  The function calculates the specific gravity of a rock mass.

  Args:
    weight_in_air: The weight of the rock mass in air.
    weight_in_water: The weight of the rock mass submerged in water.

  Returns:
    The calculated specific gravity of the rock mass.
  Raises:
    'Error: when the denominator is zero, rock weight in air can not be same when 
        weighed in water. 
  """

  try:
    specific_gravity = weight_in_air / (weight_in_air - weight_in_water)
    return specific_gravity
  except ZeroDivisionError:
    print("Error: Weight in air and weight in water cannot be the same.")
    return None

# Example usage:
weight_air = float(input("Enter the weight of the rock mass in air: "))  #requests the weight of rockmass in air.
weight_water = float(input("Enter the weight of the rock mass in water: "))

specific_gravity = calculate_specific_gravity(weight_air, weight_water)

if specific_gravity is not None:
  print(f"The specific gravity: {specific_gravity}")