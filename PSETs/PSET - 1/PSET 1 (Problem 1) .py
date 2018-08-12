# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 16:41:25 2018

@author: TheLastTitan
"""
num_vowel = 0
s = 'avsdvsa'

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        num_vowel += 1

print('Number of vowels: ' + str(num_vowel))
