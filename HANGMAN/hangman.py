# assignment: programming assignment 1
# author: Anshul Jagtap
# date: Januaray 22nd 2022
# file: hangman.py is a program that  will generate a legitimate dictionary word and ask the user to guess the word one letter at a time. The user will have restricted number of lives (attempts of guessing the word) that will be set up in the beginning of the game. After the user uses all lives or guesses the word correctly, the programs will ask the user if she wants to play again.
# input: The user will input the size and the lives, after a word has been chosen the user will get to guess the letters until their lives are over and at the end they will get a chance to chose if they wanna play again.  
# output: a random word will be chosen according to the preference a word will be chosen and it will display all the messages as the user chooses the letters one by one and depending on the choise of words the result wil be displayed.


import random
import string


dictionary_file = "dictionary.txt"



    
# main game frame which included all the conditions of the game 
def hangman_game_frame():

    count = 'Y' and 'y'
    while(count == 'Y' or count == 'y'):  #outer loop for the user to end the game or keep it going

        global lives,size,word
        word = random.choice(dictionary[size])
        word = word.upper()

        
   
        w_letters = set(word) # letters in the word to check what has been guessed
        a = set(string.ascii_uppercase)
        
        used_letters = set() # what the user has chosen/guessed

        usedlives = 0


        while len(w_letters)>0 and lives >0: # inner loop to keep on guessing until lives end
            print("Letters chosen: ", " ".join(used_letters))

                

            word_list = [l if l in used_letters else '_' for l in word]
            print("Current word:" ," ".join(word_list), "lives: ",lives, usedlives*"X"+lives*"O") 


            user_letter_choice = input("Please choose a new letter > " ).upper() # upper used because python is a case sensitive language
            if user_letter_choice in a - used_letters:
                used_letters.add(user_letter_choice)
                if user_letter_choice in w_letters:
                    w_letters.remove(user_letter_choice)
                    print("\nYou guessed right!")
                
                else:
                    lives = lives-1
                    usedlives = usedlives +1
                    print("\nYou guessed wrong, you lost one life.") 

            
            elif user_letter_choice in used_letters:
                    print("\nYou have already chosen this letter.")

               

        if lives == 0:
            print(f"You lost! The word is {word}! \n")
            break
        else:
            print(f"Congratulations!!! You won! The word is {word}! \n")
            break
    

    # for the user to decide if he wants the game to keep going
    count= input("Would you like to play again [Y/N]?")
    if(count == 'N' or count == 'n'):
        print("Goodbye!")
    elif(count == 'Y' or count == 'y'):
        size = int(input("Please choose a size of a word to be guessed [3 – 12, default any size]:"))
        lives = int(input("Please choose a number of lives [1 – 10, default 5]:"))
        return hangman_game_frame()
    
    
# creating the dictionary to efficiently search for a word from keys which represent the size of the word
def import_dictionary (dictionary_file) :
    dictionary_file = open("dictionary.txt","r")
    lst = []
    dictionary = {}
    max_size = 12

    w = dictionary_file.read()
    lst = w.split()

    for i in lst:
        if(len(i)>max_size):
            dictionary[max_size].append(i)
        elif len(i) in dictionary:
            dictionary[len(i)].append(i)
        else:
            dictionary[len(i)] = [i]            

    return dictionary


# get game options for choice of size and number of lives
def get_game_options () :
    
    global size,lives

    try:
        size = int(input("Please choose a size of a word to be guessed [3 – 12, default any size]:"))
        if(size >= 3 and size <=12):
            print(f"The word size is set to {size}.")
        else:
            print("A dictionary word of any size will be chosen.")
            size = random.randint(2,12)

    # valueerror used to take default value for size
    except ValueError:
        print("A dictionary word of any size will be chosen.")
        size = random.randint(2,12)
    
    
    try:
        lives = int(input('Please choose a number of lives [1 – 10, default 5]:'))
        if(lives>=1 and lives<=10):
            print(f"You have {lives} lives.")

    # valueerror used to take default value for lives
    except ValueError:
        lives = 5
        print("You have five lives.")    

    if(lives <1 or lives > 10):
        lives = 5
        print("You have five lives.")
            
   
    return (size, lives)



if __name__ == '__main__' :
    
    print("Welcome to the Hangman Game!")

    dictionary = import_dictionary(dictionary_file)

    get_game_options() 

    hangman_game_frame()
