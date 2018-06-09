# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 00:43:03 2018

@author: TheLastTitan
"""

num = int(input('Enter an integer to convert into binary: '))
ans = ''

if num < 0:
    negFlag = 1
    num *= -1
elif num == 0:
    ans = '0'
    negFlag = 0
else:
    negFlag = 0
    
while num > 0:
    ans = str(num%2) + ans 
    num = num // 2

if negFlag == 1:
    ans = '-' + ans
    
print(num, '=', ans, 'in binary')
    
''' 
If we use ans = ans + str(num%2), it adds the result from num%2 after the previous ans. 
So if the ans was 0 and num%2 results in 1, the ans is changed to 01, but we need the num%2
to be before the ans as it calculates the newer digits (Right to left).
'''


