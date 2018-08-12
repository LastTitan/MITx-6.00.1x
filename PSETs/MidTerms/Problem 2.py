# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:29:12 2018

@author: TheLastTitan
"""

def getSublists(L, n):
    res = []
    for x in range(len(L)-n+1):
        res.append(L[x:x+n])        
    return res

print(getSublists([1, 1, 1, 1, 4], 2))