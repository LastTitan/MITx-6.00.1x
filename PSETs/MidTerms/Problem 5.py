# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:13:13 2018

@author: TheLastTitan
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    
    res = [] 
    for i in L:
        if g(f(i)) == True:
            res.append(i)
    L[:] = res
    if L==[]:
        return -1
    else:
        return max(L)
        

def f(i):
    return i*4
def g(i):
    return i%5 == 0

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)
        
    
'''
#Example!!

def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)
Should print:

6
[5, 6]
'''