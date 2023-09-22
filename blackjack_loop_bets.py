# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 08:54:19 2023

@author: ethan.drover
"""

print("BLACKJACK!\n")
print("Blackjack payout is 3:2")
print("Enter 'x' for bet to exit\n")

start_bal = float(input("Starting money:\t\t "))
program_running = True
while program_running:
    bet_amount = (input("\nBet Amount: "))
    if bet_amount == "x":
        break # Breaks the program if user types X
    blackjack_status = str(input("Blackjack, win, push, or lose? (b,w,p,l): "))
    if blackjack_status == "b":
        start_bal = start_bal + (1.5*float(bet_amount))
        print("Money:  {}\n".format(start_bal))
    elif blackjack_status == "w":
        start_bal = start_bal + (float(bet_amount))
        print("Money:  {}\n".format(start_bal))
    elif blackjack_status == "p":
        start_bal = start_bal
        print("Money:  {}\n".format(start_bal))
    elif blackjack_status == "l":
        start_bal = (start_bal - float(bet_amount))
        print("Money:  {}\n".format(start_bal))

print("Bye!")