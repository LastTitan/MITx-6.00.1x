# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:36:02 2018

@author: TheLastTitan
"""
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord = list(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            secretWord[i] = '_'
            
    return ' '.join(secretWord)
                
        
secretWord = 'else' 
lettersGuessed = ['e', 's']
print(getGuessedWord(secretWord, lettersGuessed))

