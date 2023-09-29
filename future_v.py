# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:42:25 2023

@author: ethan.drover
"""



def future_value(monthly_invest,year_rate,years):
    """
    

    Parameters
    ----------
    monthly_invest : Float
        DESCRIPTION.
    year_rate : TYPE
        DESCRIPTION.
    years : TYPE
        DESCRIPTION.

    Returns
    -------
    f_value : TYPE
        DESCRIPTION.

    """
    m_time = years *12
    m_int_rt = year_rate / 12
    f_value = 0
    for i in range(m_time):
        f_value = monthly_invest + f_value
        f_value += (f_value * m_int_rt)/100
    return f_value

if __name__ == "__main__":
    continue_loop = 'y'
    while continue_loop.lower() == 'y':
        monthly_invest = float(input("\nEnter monthly investment:\t\t"))
        year_rate = float(input("Enter yearly interest rate:\t\t"))
        years = int(input("Enter number of years:\t\t\t"))
        future_val = future_value(monthly_invest, year_rate, years)
        print("Future value:\t\t\t\t\t{}".format(future_val))
    
    
    