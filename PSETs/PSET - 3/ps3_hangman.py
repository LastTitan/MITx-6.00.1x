# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
   
    a = set(secretWord)
    b = set(lettersGuessed)  
    return a.issubset(b)

def getGuessedWord(secretWord, lettersGuessed):
    
    secretWord = list(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            secretWord[i] = '_'
            
    return (' '.join(secretWord))

def getAvailableLetters(lettersGuessed):
    
    s = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        s.remove(letter)
        
    return (''.join(s))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessLeft = 8
    lettersGuessed = []
    print ('Welcome to the game, Hangman!')
    print('I am thinking of a word that is',len(secretWord), 'letters long.')    
    
    while guessLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        
        print('-'*11)
        print('You have', guessLeft, 'guesses left.')
        print('Available letters:',getAvailableLetters(lettersGuessed)) 
        guess =  input('Please guess a letter: ')   
        guess = guess.lower()
        
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord,lettersGuessed))
        else:
            lettersGuessed.append(guess)
            
            if guess.lower() in secretWord:
                print('Good guess:',getGuessedWord(secretWord,lettersGuessed))
            else:
                guessLeft -= 1
                print('Oops! That letter is not in my word:',getGuessedWord(secretWord,lettersGuessed) )
         
    print('-'*11)
    if guessLeft > 0:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was', secretWord + '.')               

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
