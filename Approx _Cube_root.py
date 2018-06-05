# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

cube = float(input('Enter any number to calculate the cube root: '))
check = 0.01
increment = 0.001
num_guess = 0
guess = 0

while abs(guess**3 - abs(cube)) >= check and guess <= cube:
    guess += increment
    num_guess += 1

if abs(guess**3 - abs(cube)) >= check:
    print ('failed to calculate the cube root of', cube)
    
elif guess**3 != abs(cube):
   
    if cube < 0:
        guess *= -1
   
    print(guess, 'is the approximate cube root of', cube)

print('Total guesses =', num_guess)    
    
        