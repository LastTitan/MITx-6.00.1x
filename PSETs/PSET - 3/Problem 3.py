# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:33:15 2018

@author: TheLastTitan
"""
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        s.remove(letter)
        
    return ''.join(s)

l = ['a', 'b', 'd']
print(getAvailableLetters(l))