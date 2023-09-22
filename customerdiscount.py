# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:13:05 2023

@author: ethan.drover
"""
# Customer type and input type for customer to type
customer_type = input("Enter customer type (R or W):  ")
invoice_total = float(input("\nEnter the amount on your invoice:  "))
if customer_type.lower() == "r": 
    if invoice_total < 250:
        discount_percent = 0
    elif invoice_total >= 250:
        discount_percent = .02
elif customer_type.lower() == "w":
        discount_percent = .04
else:
    print("Customer type must be R or W")

invoice_final = (invoice_total) - (invoice_total) * (discount_percent)
print("\nYour invoice price:\t\t{}".format(invoice_total))
print("Discount Percentage:\t{}".format(discount_percent))
print("Discount Amount:\t\t{}".format(invoice_final-invoice_total))
print("New Invoice total:\t\t{}".format(invoice_final))