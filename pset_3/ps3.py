# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <Alejandro Corrales Morillas>
# Collaborators : <your collaborators>
# Time spent    : <8 hours>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    letters_points = 0
    #First component
    for i in word:
        letters_points += SCRABBLE_LETTER_VALUES[i]
    #Second component
    hand_value = (7 * len(word) - 3 * (n - len(word)))
    if hand_value > 1:
        return letters_points * hand_value
    else:
        return letters_points            

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    wild_card = 1

    for i in range(num_vowels):
        if i == 1:
            hand['*'] = 1
        else:
            x = random.choice(VOWELS)
            hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word = word.lower()
    new_hand = hand.copy()
    for letter in word:
        if letter in new_hand:
            new_hand[letter] -= 1
            if new_hand[letter] <= 0:
                new_hand.pop(letter)
    
    return new_hand
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    copy_hand = hand.copy()
    
    #Including wildcard
    x = word.find("*")
    list = []
    for i in VOWELS:
        if '*' in word:
            newWord = word.replace('*', i)
            list.append(newWord)
        else:
            list.append(word)
            break     

    wild_card = False
            
    for i in list:
        if i in word_list:
            wild_card = True
    
    #Check if word in hand
    word_in_hand = True
    for i in word:
        if i not in copy_hand:
            word_in_hand = False
            break
        elif i in copy_hand:
            copy_hand[i] = copy_hand[i] - 1
            if copy_hand[i] <= 0:
                copy_hand.pop(i)
                
    word_find = False  
            
    for word_ls in list:
        if (word_ls.isalpha()) and (word_ls in word_list) and (word_in_hand == True) and (wild_card == True):
            word_find = True
        
    if word_find == True:
        return True
    else:
        return False

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    sum = 0
    for k in hand:
        sum = sum + hand.get(k, 0)
        
    return sum 
    

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    total_score = 0
    n = 7
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        print("Current hand: ", end = '')
        display_hand(hand)

        # Ask user for input
        word = input("Enter word, or '!!' to indicate that you are finished: ")
        
        # If the input is two exclamation points:
        if word == '!!':
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list):
                # Tell the user how many points the word earned,
                # and the updated total score
                score_word = get_word_score(word, n)
                total_score += score_word
                print("'" + word + "'", "earned", score_word, "points. Total:", total_score)
                print()

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.")
                print()
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)
            
    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    if calculate_handlen(hand) > 0:
        print("Total score for this hand:", total_score)
        print("_" * 30)
    else:
        print("Ran out of letters.")
        print("Total score for this hand:", total_score)
        print("_" * 30)

    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    #See if letter is already in the hand or not:
    #If is True
    
    if letter not in hand:
        #Return the given hand
        return hand
    #If is False
    else:
        #Check if random letter not in hand 
        while True:
            x = random.choice(VOWELS + CONSONANTS)
            if x not in hand:
                break
        #Update the hand 
        new_hand = {}  
        for i in hand:
            if i == letter:
                hand.update({x:hand[letter]})
                hand.pop(letter)
                break
        #Return the updated hand
        return hand
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    print("_" * 30)
    #ask the user to input a total number of hands
    total_hands = int(input("Enter total number of hands: "))
    #INItoalize variable for recording total scores of all hands
    score_total_hands = 0
     #initalize variable to record the substitution option validity, this is can be done once during the game, so they are written outslide number of hands loop
    sub_valid = True
     #initalize varibale for recording replaying preference, this is can be done once during the game, so they are written outslide number of hands loop
    replay_validity = True
    #playing n hands according to user choice
    for i in range(0, total_hands):
        #for each hand:       
        #get the hand
        current_hand = deal_hand(HAND_SIZE)
        #list the two possible scores of a hand
        current_hand_scores = [0, 0]
        #initialize variable for recording the tries of playing the same hand
        current_hand_try = 0
        #initalize variable for recording user prefernece for replying the current hand
        current_replay_pref = True
        #test for replaying preference and number of tries is less that two, as replaying can be done only once
        while (current_replay_pref and (current_hand_try < 2)):
            #if replaying is valid, play again
            print("Current hand: ", end = '')
            display_hand(current_hand)
            # if there are two conditions and one is after the other, then make nested loop, with outer loop is the first condition and inner loop the second consequent condition
            #test for substitution validity and user prefernce for sub
            if sub_valid:
                #ask for user if s/he wants to substitute a letter
                us_sub_pref = input("Would you like to substitute a letter? ").lower()
                if (us_sub_pref == "yes"):
                    #ask which letter and do the substituion, 
                    user_sub_letter = input("Which letter would you like to replace: ")
                    current_hand = substitute_hand(current_hand, user_sub_letter)
                    sub_valid = False
                else:
                    pass
            else:
                pass
            #let the user play the game with hand
#Note of fails:
# here, if you want to do the function and use its return function later, you should store its return value in a varibale, because if you call it again in position where you want to use its return value, it will excute again and have return value other than one upo had from the past call
            print()
            score_current_try = play_hand(current_hand, word_list)
            #store the score of the play trial at ithe list of possible scores variable using the number tries variable as the index number
            current_hand_scores[current_hand_try] = score_current_try
            #tell user score of this hand try
            print("Total score for this hand try:", current_hand_scores[(current_hand_try)])
# if there are two conditions and one is after the other, then make nested loop, with outer loop is the first condition and inner loop the second consequent condition
            if replay_validity:
                #test for replaying preference,
                print("-------------------------------------------------------------")
                us_replaying_pref = input("Would you like to replay the hand? ").lower()
                 #if so ask the user if they would like to replay the hand. and increase number of rails by 1
                if (us_replaying_pref == "yes"):
                    current_hand_try += 1
                    # tuen replaying option false as replaying can be done only ONCE DURING THE GAME
                    replay_validity = False
                    sub_valid = False
                else:
                    current_replay_pref = False
            #otherwise, turn replaying preference of the current hand to false
            else:
                current_replay_pref = False
            
        #add the hisghest score of two tries to the total score
        if current_hand_scores[0] > current_hand_scores[1]:
            #tell user the highest score for this hand that will be added to the final score
            print("Hand score that will be added to overall score is:", current_hand_scores[0])
            score_total_hands += current_hand_scores[0]
        else:
            #tell user the highest score for this hand that will be added to the final score
            print("Hand score that will be added to overall score is:", current_hand_scores[1])
            score_total_hands += current_hand_scores[1]
        #play the next hand
        print("End of Hand number:", (i+1), "------------------------------------------------------------")
    # return the total score for all hand series
    print("Total score over all hands:", score_total_hands)
    print("End of the Game. Hope you enjoyed it. :)")
        
    return score_total_hands        
            
        
#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    
