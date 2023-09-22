# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:24:43 2023

@author: ethan.drover
"""

print("The Test Scores Program by Ethan Drover\n")
print("Enter 3 Test Scores")
print(13*"-=")
test_score1 = float(input("Enter test score 1: "))
test_score2 = float(input("Enter test score 2: "))
test_score3 = float(input("Enter test score 3: "))
test_score4 = float(input("Enter test score 4: "))
print(13*"-=")
total_score = (test_score1 + test_score2 + test_score3)
average_score = (total_score / 4)
print("Total Score:\t\t",(total_score))
print("Average Score:\t\t",(average_score))
print("\nBye!")