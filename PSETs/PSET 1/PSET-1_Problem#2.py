# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 16:41:50 2018

@author: TheLastTian
"""

count = 0
index = 0 

while index < len(s):
    if s[index] == 'b':
        if index+2 < len(s):
            if s[index+1] == 'o':
                if s[index+2] == 'b':
                    count +=1
    index += 1

print('Number of times bob occurs is: ' + str(count) )
                
