#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def calculate_specific_gravity(weight_in_air, weight_in_water):
    """
    The function calculates the specific gravity of a rock mass.

  Args:
    weight_in_air: Takes float weight of the rock mass in air.
    weight_in_water: Takes float weight of the rock mass submerged in water.

  Returns:
    The calculated float specific gravity of the rock mass.
  Raises:
    'Error: when the denominator is zero, rock weight in air can not be same when 
        weighed in water. 
  >>> calculate_specific_gravity(2, 2)
      "Error: recheck your measurements."
  >>> calculate_specific_gravity(4, 2)
      specific gravity:2.0
  >>> calculate_specific_gravity(5, 2)  
      specific gravity: 1.6666666666666667
    """
    if weight_in_air <= weight_in_water:        #checks the equality of the inputs:
      #throws error: rock mass weighed in open air should be > in weighed in water:
        return "Error: recheck your measurements."
      #if not equal->the specific gravity is calculated below:
    specific_gravity = weight_in_air / (weight_in_air - weight_in_water) 
    return f"specific gravity: {specific_gravity}"   #keeps the value of specific gravity

# Takes a weight measurements into float to comply with scientific notation:
weight_air = float(input("Enter weight of the rock mass in air: "))
weight_water = float(input("Enter weight of the rock mass in water: "))

# get the result message
result_message = calculate_specific_gravity(weight_air, weight_water)
