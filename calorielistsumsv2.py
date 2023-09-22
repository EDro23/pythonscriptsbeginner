# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 08:26:01 2023

@author: ethan.drover
"""

def countCalories():
    input_txt = open('input.txt', 'r')
    lines = input_txt.readlines()
    
    """ for line in lines: #Checking to see if input is working
        print(line)"""
    
 
    sumCalories = 0
    listCaloriesSums=[]
    
    for line in lines:
        #If the line is blank in text return added sums to list
        if line.strip()=="":
            listCaloriesSums.append(sumCalories)
            sumCalories = 0
            #If the line is not blank, keep adding until you reach a blank.
        else:
            sumCalories += int(line)
            
    print(max(listCaloriesSums))

listCaloriesSums=[]

listCaloriesSums.sort(sorted,reversed = True)
sumTopThree=listCaloriesSums[0]+listCaloriesSums[1]+listCaloriesSums[2]

print(sumTopThree)

countCalories()