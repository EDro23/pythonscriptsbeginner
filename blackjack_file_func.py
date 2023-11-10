# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:55:35 2023

@author: ethan.drover
"""

def write_money(amount):
    with open('money.txt','w') as ethans_file:
        ethans_file.write(str(amount))
    
def read_money():
    with open('money.txt') as someones_wallet:
        money = someones_wallet.read()
        return int(money)