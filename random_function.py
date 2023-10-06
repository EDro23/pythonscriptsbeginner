# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:31:58 2023

@author: ethan.drover
"""

import random


# Random function
# float 0.0 and 1.0
number1 = random.random() * 100
print(number1)

# The randint() function
# int in the range you specify
# Syntax: randint(min, max)

number2 = random.randint(201,300)
print(number2)

# The randrange() function
# int in the range that you specify
# Syntax: randrange([Start,] stop[,step])
# Step meaning increments of which to pick from

number3 = random.randrange(1,100)
print(number3)

number5 = random.randrange(100, 200, 2)
print(number5)
