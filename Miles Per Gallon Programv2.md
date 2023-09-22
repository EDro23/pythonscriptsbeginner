# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:24:42 2023

@author: ethan.drover
"""
print("\nThe Miles Per Gallon Program")
Miles_Driven = float(input("Enter miles driven:            "))
gallons = float(input("Enter gallons of gas used:     "))
Miles_per_gallon = (Miles_Driven) / (gallons)
print("\nMiles per Gallon:              {:.2f}".format(Miles_per_gallon))
print("\nBye!")
