# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:24:43 2023

@author: ethan.drover
"""

print("\n\nThe Test Scores Program by Ethan Drover\n")
print("Enter 3 Test Scores")
print(13*"-=")
test_score1 = int(input("Enter test score 1: "))
test_score2 = int(input("Enter test score 2: "))
test_score3 = int(input("Enter test score 3: "))
print(13*"-=")
total_score = (test_score1 + test_score2 + test_score3)
average_score = (total_score / 3)

    
print("Total Score:\t\t",(total_score))
print("Average Score:\t\t",(average_score))

if average_score >= 90 and average_score <= 100:
        print ("Average grade: \t\tA")
elif average_score >= 80 and average_score <= 89:
    print ("Average grade: \t\tB")
elif average_score >= 60 and average_score <= 79:
    print ("Average grade:  \t\tC")
elif average_score >= 40 and average_score <= 59:
    print ("Average grade: \t\tD")
elif average_score < 40:
    print ("Average grade: \t\tF")

    
print("\nBye!")