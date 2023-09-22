# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 08:43:05 2023

@author: ethan.drover
"""
# All console inuts for name, number of bats, number of hits.

name = (input("Please enter your name: "))
number_batting = int(input("Official number of at bats: "))
hits = (int(input("Number of hits: ")))

batting_average = (hits / number_batting) #Calculation for average batting

print(50*"=") #Decoration
print("\t\t\t\tBaseball Team Manager")
print("""\nThis program calculates the batting average for a player based 
      on the player's official number of bats and hits.""")
print(50*"=") #Decoration
print("Player's name: {}".format(name))
print("official number of at bats: {}".format(number_batting))
print("Number of hits: {}".format(hits))
print("\n{}'s batting average is: {:.3f}".format(name,batting_average))