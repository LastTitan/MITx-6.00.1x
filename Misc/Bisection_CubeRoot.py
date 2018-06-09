# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 16:42:22 2018

@author: TheLastTitan
"""

x = float(input("Enter an integer to calculate the cube root of: "))
check = 0.01 
count = 0

if abs(x) >= 1:
    
    if x < 0:
        x *= -1
        neg = 1
    else:
        neg = 0
        
    low = 1
    high = x
    ans = (low + high)/2
    
    while abs(ans**3 - x) >= check:
        
        count += 1
        print ('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str (ans))
        
        if ans**3 > x:
            high = ans
        
        elif ans**3 < x:
            low = ans
            
        ans = (low + high)/2
        
    if neg == 1:
        ans *= -1
        
    print ('The cube root of ' + str(x) + ' is ' + str(ans))    
    print ('Total checks = ' + str(count))        

elif 0 < abs(x) < 1:
    
    if x < 0:
       x *= -1
       neg = 1
    else:
       neg = 0
    
    low = 0
    high = x
    ans = (low + high)/2

    while abs(ans**3 - x) >= 0.05: #due to storage limitations of int, we need to increase the error check, otherwise it'll become an infinite loop
        
        count += 1
        print ('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str (ans))
        
        if ans**3 > x:
            
            low = 0
            high = ans
        
        elif ans**3 < x:
            
            low = ans
            high = 1
        
        ans = (low + high)/2
                    
    if neg == 1:
        ans *= -1
        
    print ('The cube root of ' + str(x) + ' is ' + str(ans))    
    print ('Total checks = ' + str(count))