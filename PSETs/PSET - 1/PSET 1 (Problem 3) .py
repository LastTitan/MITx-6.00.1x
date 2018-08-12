# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 09:17:42 2018

@author: TheLastTitan
"""

s = 'lbpbcjmosufus'
ans = s[0]
new_str = ''

for i in range (len(s)-1):
    
    j = i+1;
    k = i;
    
    while s[k] <= s[j] and (k <= (len(s)-2) and j <= (len(s)-2)):
        new_str = s[i:j+1]
        k += 1; j += 1;
        
        if k == len(s) - 2:
            if s[k] < s[-1]:
                new_str += s[-1]
            
    
    if len(new_str) > len (ans):
        ans = new_str;
        
print ('Longest substring in alphabetical order is: ' + ans)

