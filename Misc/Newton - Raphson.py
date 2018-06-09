# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 23:26:43 2018

@author: TheLastTitan
"""

x = int(input('Enter a number to calculate the square root of: '))

if x < 0:
    print ('No real square root exists!')
    
else:
    check = 0.01
    num_guess = 0
    guess = x/2
    
    while abs(guess**2 - x) >= check:
        num_guess += 1
        guess = guess - ((guess**2) - x)/(2*guess)
        print ('num_guess =', num_guess, 'guess =', guess, 'remainder =',guess**2 - x)
    
    print('Total number of guesses = ' + str(num_guess))
    print('Square root of', x, 'is approximately =', guess)
    
    
#Actually the first guess is x/2 but we have considered the number of iterations of while loop for num_guess.