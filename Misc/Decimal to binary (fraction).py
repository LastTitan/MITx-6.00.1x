# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 01:16:44 2018

@author: TheLastTitan
"""

x = float(input('Enter a decimal number between 0 and 1 to convert into binary: '))
p = 0
ans = ''

if x < 0:
    negFlag = 1
    x *= -1
elif x == 0.0:
    ans = '0'
    negFlag = 0
else:
    negFlag = 0
        
while (2**p)*x % 1 != 0:
    print('P =', p,(2**p)*x ,'Remainder =', ((2**p)*x - int((2**p)*x)))
    p += 1;
    
num = int((2**p)*x)

while num > 0:
    ans = str(num%2) + ans 
    num = num // 2

ans = float(ans)

if negFlag == 1:
    ans *= -1
    
print(num, '=', ans/(10**p), 'in binary')