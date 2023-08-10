# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent: 6:55 -  
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    for i in secret_word:
          if i in letters_guessed:
                count += 1
    if count == len(secret_word):
          return True
    else:
          return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = []   
    for i in secret_word:
          if i in letters_guessed:
                guess.append(i)
          else:
                guess.append("_ ")
 
    return "".join(guess)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    alphabet_lower = list(string.ascii_lowercase)
    
    for i in letters_guessed:
        if i in alphabet_lower:
            alphabet_lower.remove(i)
            
    return "".join(alphabet_lower)
                
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have 3 warnings left.")
    print("-" * 13)
    print("You have 6 guesses left.")
    print("Available letters: abcdefghijklmnopqrstuvwxyz")
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    letters_guessed = []
    unique_letters = []
    w = 3 #number of warning
    g = 6 #number of guesses
    
    total_score = g * len(unique_letters)
    
    while g > 0:
          letter = input("Please guess a letter: ").lower()
          if letter.isalpha():
                #If you guessed the letter already:
                if letter in letters_guessed:
                    if w >= 1:
                          w -= 1
                          print("Oops! You've already guessed that letter. You have", w, "warnings left :")
                          print(get_guessed_word(secret_word, letters_guessed))
                          print("-" * 13)
                          print("You have", g, "guesses left.")
                          print("Available letters:", get_available_letters(letters_guessed))
                    else:
                          g -= 1
                          print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed)) 
                          print("-" * 13)
                          if g > 0:
                              print("You have", g, "guesses left.")
                              print("Available letters:", get_available_letters(letters_guessed))
                              w = 3    
                          
                #If you guess a letter:            
                elif letter in secret_word:
                    letters_guessed.append(letter)
                    #Unique letters:
                    if is_word_guessed(secret_word, letters_guessed):
                        for i in get_guessed_word(secret_word, letters_guessed):
                            if i not in unique_letters:
                                  unique_letters.append(i)
                        unique_letters.remove("'")
                        total_score = g * len(unique_letters)
                        
                    #If you win the game:  
                    if is_word_guessed(secret_word, letters_guessed):
                          print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                          print("-" * 13)
                          print("Congratulations, you won!")
                          print("Your total score for this game is: " + str(total_score)) #I think this should be a return.
                          break
                    #If you guess the letter:
                    else:   
                          print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                          print("-" * 13)
                          print("You have", g, "guesses left.")
                          print("Available letters:", get_available_letters(letters_guessed))         
                #If you don't guess a letter:          
                else:
                    letters_guessed.append(letter)
                    if letter not in vowels:
                          g -= 1
                          print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                          print("-" * 13)
                          if g > 0:
                              print("You have", g, "guesses left.")
                              print("Available letters:", get_available_letters(letters_guessed)) 
                    elif letter in vowels:
                          g -= 2
                          print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                          print("-" * 13)
                          if g > 0:
                              print("You have", g, "guesses left.")
                              print("Available letters:", get_available_letters(letters_guessed))
                          
          #If you enter a non-alph character:
          else:
                w -= 1
                if w == 0:
                      g -= 1
                      print("You have 0 warnings left. You lose 1 guess.")
                      print("You have", g, "guesses left.")
                      w = 3
                else:
                      print("Oops! That's not a valid letter. You have", w, "warning left." + get_guessed_word(secret_word, letters_guessed))
                      print("-" * 13)
                      print("You have", g, "guesses left.")
                      print("Available letters:", get_available_letters(letters_guessed))
          #If you lose the game:            
          if g <= 0:
                print("Sorry, you ran out of guesses. The word was " + secret_word + ".")#I think this should be a return too.



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.split()
    my_word = "".join(my_word)
    # Check if the two words are the same length
    if len(my_word) != len(other_word):
        return False
    
    # Check if the guessed letters in my_word match the corresponding letters in other_word
    for i in range(len(my_word)):
        if my_word[i] != '_' and my_word[i] != other_word[i]:
            return False
        elif my_word[i] == '_' and other_word[i] in my_word:
              return False
    
      # If the function has not returned False yet, it means that the two words match
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
        
    #Seek the matches in the worldlist:
    for i in wordlist:
        if match_with_gaps(my_word, i) == True:
            possible_matches.append(i)
                
    #If there's no match, print it: 
    if len(possible_matches) == 0:
        return "No matches found" #Watch out the returns
    #Print the matches:
    else:
        possible_matches = " ".join(possible_matches)
        return possible_matches #Watch out the returns



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have 3 warnings left.")
    print("-" * 13)
    print("You have 6 guesses left.")
    print("Available letters: abcdefghijklmnopqrstuvwxyz")
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    letters_guessed = []
    unique_letters = []
    w = 3 #number of warning
    g = 6 #number of guesses
    
    total_score = g * len(unique_letters)
    
    while g > 0:
          letter = input("Please guess a letter: ").lower()
          if letter.isalpha() or letter == "*":
                #Hints:    
                if letter == "*":
                      print("Possible word matches are:")
                      print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                      print("-" * 13)
                      print("You have", g, "guesses left.")
                      print("Available letters:", get_available_letters(letters_guessed))
                #If you guessed the letter already:
                if letter in letters_guessed and letter != "*":
                    if w >= 1:
                          w -= 1
                          print("Oops! You've already guessed that letter. You have", w, "warnings left :")
                          print(get_guessed_word(secret_word, letters_guessed))
                          print("-" * 13)
                          print("You have", g, "guesses left.")
                          print("Available letters:", get_available_letters(letters_guessed))
                    else:
                          g -= 1
                          print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed)) 
                          print("-" * 13)
                          if g > 0:
                              print("You have", g, "guesses left.")
                              print("Available letters:", get_available_letters(letters_guessed))
                              w = 3    
                          
                #If you guess a letter:            
                elif letter in secret_word and letter != "*":
                    letters_guessed.append(letter)
                    #Unique letters:
                    if is_word_guessed(secret_word, letters_guessed):
                        for i in get_guessed_word(secret_word, letters_guessed):
                            if i not in unique_letters:
                                  unique_letters.append(i)
                        total_score = g * len(unique_letters)
                        
                    #If you win the game:  
                    if is_word_guessed(secret_word, letters_guessed):
                          print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                          print("-" * 13)
                          print("Congratulations, you won!")
                          print("Your total score for this game is: " + str(total_score)) #I think this should be a return.
                          break
                    #If you guess the letter:
                    else:   
                          print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                          print("-" * 13)
                          print("You have", g, "guesses left.")
                          print("Available letters:", get_available_letters(letters_guessed))         
                #If you don't guess a letter:          
                elif letter != "*":
                    letters_guessed.append(letter)
                    if letter not in vowels:
                          g -= 1
                          print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                          print("-" * 13)
                          if g > 0:
                              print("You have", g, "guesses left.")
                              print("Available letters:", get_available_letters(letters_guessed)) 
                    elif letter in vowels:
                          g -= 2
                          print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                          print("-" * 13)
                          if g > 0:
                              print("You have", g, "guesses left.")
                              print("Available letters:", get_available_letters(letters_guessed))
                          
          #If you enter a non-alph character:
          else:
                w -= 1
                if w == 0:
                      g -= 1
                      print("You have 0 warnings left. You lose 1 guess.")
                      print("You have", g, "guesses left.")
                      w = 3
                else:
                      print("Oops! That's not a valid letter. You have", w, "warning left." + get_guessed_word(secret_word, letters_guessed))
                      print("-" * 13)
                      print("You have", g, "guesses left.")
                      print("Available letters:", get_available_letters(letters_guessed))
          #If you lose the game:            
          if g <= 0:
                print("Sorry, you ran out of guesses. The word was " + secret_word + ".")#I think this should be a return too.



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    answer = input("Do you want to play with hints, yes or no? (y/n): ").lower()
    if answer == "n":
          secret_word = choose_word(wordlist)
          hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    elif answer == "y":
          secret_word = choose_word(wordlist)
          hangman_with_hints(secret_word)
