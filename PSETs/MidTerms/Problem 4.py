# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:05:33 2018

@author: TheLastTitan
"""

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N%10 == N:
        return N
    else:
        return sumDigits(N//10) + N%10
    