# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 08:53:53 2018

@author: TheLastTitan
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    a = set(secretWord)
    b = set(lettersGuessed)  
    return a.issubset(b)
    
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'l', 's', 'q', 't', 'a']
print(isWordGuessed(secretWord, lettersGuessed))

#Solution 2

'''
def isWordGuessed(secretWord, lettersGuessed):
    
   secretWord = list(secretWord)
        
    for letter in lettersGuessed:
        if letter in secretWord:
            while letter in secretWord:
                secretWord.remove(letter)
    return len(secretWord)==0

'''
     
     
    