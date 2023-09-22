# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:14:00 2023

@author: ethan.drover
"""

print("BLACKJACK!\n")
print("Blackjack payout is 3:2")
print("Enter 'x' for bet to exit\n")

start_balance = float(input("Starting money:\t\t "))
bet_amount = float(input("Bet amount:\t\t\t "))
b = (bet_amount * 1.5)
w = (start_balance + bet_amount)
p = (start_balance)
l = (start_balance - bet_amount)

while bet_amount == int:
    
    if input == b:
        start_balance + b
    elif input == w:
        start_balance + bet_amount
    elif input == p:
        start_balance
    elif input == l:
        start_balance - bet_amount
        