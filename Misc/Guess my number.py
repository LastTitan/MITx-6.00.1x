# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:20:54 2018

@author: TheLastTitan
"""
def n(x):
    return x+1

print('Please think of a secret number between 0 and 100!')
inp = ''
high = 100
low = 0 
while inp != 'c':
    ans = (high+low)//2
    print('Is your secret number',ans,'?')
    inp = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly. ')
    if inp == 'h':
        high = ans
    elif  inp == 'l':
        low = ans
    elif inp == 'c':
        print('Game over. Your secret number was:', ans)
        break
    else:
        print('Sorry, I did not understand your input.')
