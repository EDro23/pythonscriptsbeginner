#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:37:58 2023

@author: kaileyslaney
"""

print(60*"=")
print("Shipping calculator")
print(60*"=")

def shippingcalculator():
    item_cost = float(input("Cost of items ordered: "))
    ship_cost = float(input("Shipping cost: "))
    total = float(input("Total cost: "))
    program_run = True    
    total = 0
    ship_cost = 0
    while program_run:
        if item_cost < 30:
            ship_cost = 5.95
        elif item_cost >= 30:
            ship_cost = 7.95
            print("Total cost: {}".format(total))
    while True:
        if input("\nContinue? (y/n): ").lower() != "y":
            print("\nBye!")
        break
    
                
"""
    elif:
        item_cost <= 30 or >= 49.99:
            ship_cost = 7.95
    elif:
        item_cost <= 50 or >= 74.99:
            ship_cost = 9.95
    else:
        ship_cost = 0"""
        
                  