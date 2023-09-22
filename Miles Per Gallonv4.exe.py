# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:04:54 2023

@author: ethan.drover
"""

print("\n\nThe Miles Per Gallon Program\n")
Miles_Driven = float(input("Enter miles driven:\t\t\t\t"))
gallons = float(input("Enter gallons of gas used:\t\t"))
if (gallons <= 0):
  print(22 * "-")
  print("Gallons used must be greater than Zero. Try again.")
  print(22 * "-")
    


else:
     Miles_per_gallon = (Miles_Driven) / (gallons)
     print("\nMiles per Gallon:\t\t\t\t{:.2f}".format(Miles_per_gallon))
     print("\nBye, have a good day!")     
    


