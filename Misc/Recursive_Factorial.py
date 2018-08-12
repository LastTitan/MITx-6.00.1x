# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 22:33:17 2018

@author: TheLastTitan
"""

def fact(a):
    if a == 1:
        return 1
    else:
        return a*fact(a-1)

print(fact(5))