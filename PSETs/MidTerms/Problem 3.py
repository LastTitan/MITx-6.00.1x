# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:58:18 2018

@author: TheLastTitan
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    res = []
    for elmt in aDict:
        if aDict[elmt] == target:
            res.append(elmt)
            
    return sorted(res)

a = {1:10, 3:20 , 4:50, 2:20, 6:20, 5:20, 8:60}
b = 20

keysWithValue(a,b)
