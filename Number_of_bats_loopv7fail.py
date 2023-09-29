# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:43:45 2023

@author: ethan.drover
"""

def main():
    
    def title():
        print(50*'=')
        
        print("\t\t\tBaseball Team Manager")
    def menu():
        print("MENU OPTIONS")
        print("1 - Calculate batting average")
        print("2 - Exit program")
        
        print(50*"=")
    def number_of_bats():
        program_running = True
        while program_running:
            menu = int(input("Menu Option: "))
            if menu == 1:
        
                number_of_bats = float(input("Official number of at bats: "))
                hits = float(input("Number of hits: "))
                batting_a = (hits / number_of_bats)
                print("Batting average is: {:.3f}\n".format(batting_a))
        
            elif menu != 1:
                break
        else:
                print("\nThis is not a valid option.")
                
    if __name__ is "__main__":
        
        






