# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:03:38 2018

@author: TheLastTitan
"""
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if x == 1 or x < b:
        return 0
    elif x == b:
        return 1
    else:
        return myLog(x/b,b) + 1
    