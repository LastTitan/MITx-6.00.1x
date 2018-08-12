# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 00:28:42 2018

@author: TheLastTitan
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
  
    if len(aStr) == 0:
        return False
    
    elif len(aStr) == 1: 
        return char == aStr
    
    else:
        mid = len(aStr)//2
        if aStr[mid] == char:
            return True
        elif char > aStr[mid] : 
            return(isIn(char,aStr[(mid)+1:]))     
        else : 
            return(isIn(char,aStr[:(mid)]))
    
print(isIn('a','abc'))