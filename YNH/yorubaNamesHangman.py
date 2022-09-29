# First import libaries
from ast import While
import random
#import the names
from yorubaNames import yorubaNames
import string

# Creating a function that gets the name
def get_valid_names(yorubaNames):
    name = random.choice(yorubaNames) # choose random name from list
    while '-' in name or ' ' in name:
        name = random.choice(yorubaNames)
    return name

# define hangman
def hangman():
    # make names uppercase
    name = get_valid_names(yorubaNames)
    name = name.upper()
    # create varable that saves the letters of a name as a set
    name_letters = set(name) #letters guessed in name
    #import predetermined list of uppercase charcters in english dictionary
    alphabet = set(string.ascii_uppercase)
    # create empty set to keep track of what the user has guessed
    used_letters = set() # what user has guessed

    # Define Number of Lives
    lives = 10

    # getting user input
    while len(name_letters) > 0 and lives > 0:
        #letters used
        print('You have', lives ,' lives left','You have used these letters: ', ' '.join(used_letters))

        # what current name is 

        name_list = [letter if letter in used_letters else '-' for letter in name]
        print('Current:', ''.join(name_list))

    # getting user input
        user_letter = input('Guess a Yoruba Name:').upper()
    # if the alphabet has not been used add to used set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
        # if letter was in the name remove that letter from name letters
            if user_letter in name_letters:
                name_letters.remove(user_letter)
            else:
                lives = lives - 1 # takes lives away
                print('This letter is not in the name.  o.o')
    # if user inputs same letter
        elif user_letter in used_letters:
            print('You have guessed that letter')
        else:
            print('Invalid Character. Please try again. ')
#exits when name letters and lives  == 0   
    if lives == 0:
        print("Sorry you have died, the name was ", name)
        print('Better luck next time.')
    else: 
        print("Congrats!!! UwU")
        print('You have guessed the correct name', name)


hangman()


