# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 08:26:01 2023

@author: ethan.drover
"""

def countCalories():
    input_txt = open('input.txt', 'r')
    lines = input_txt.readlines()
    
    """ for line in lines:
        print(line)"""
    
 
    sumCalories = 0
    listCaloriesSums=[]
    
    for line in lines:
        
        if line.strip()=="":
            listCaloriesSums.append(sumCalories)
            sumCalories = 0
            
        else:
            sumCalories += int(line)
            
    print(max(listCaloriesSums))
    
countCalories()
