# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:51:49 2023

@author: ethan.drover
"""

import random
program = True


def title():
    print("Guess the Number!")
    print("\nI'm thinking of a number from 1 to 10")
    
    
def user_guess():
    count = 1
    randomint = random.randrange(1,10)
    while program:
        guess = int(input("Your guess: "))
        
 
        if guess < randomint:
            print("Too low")
            
        elif guess > randomint:
            print("Too high")
        
        else: 
            guess

            print("You guessed it in {} tries".format(count))
            if input("\nWould you like to play again? (y/n):  ") != 'y' and 'Y':
                break
            else:
                randomint = random.randrange(1,10)
                count = 0
        count += 1
    
def main():
    title()
    user_guess()
    print("\nBye!")
    
if __name__ == '__main__': 
    main()



   
    
