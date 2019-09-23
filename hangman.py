#create list of words that will be randomly selected for the game
import random

words_list = ["TOMATO", "AVOCADO", "SAMPHIRE", "BRAZIL NUT", "BROCCOLI", "CHICKPEA", "SHALLOTS", "WATERMELON", "BOK CHOI"]

hidden_word = random.choice(words_list)



print ("HELLO, AND WELCOME TO HANGMAN!")
name = input("What is your name? ").strip()
print ("Hello, " + name + "!")
print ("""The aim of the game is to guess the hidden word.
You have 10 lives - each time you guess a letter that is not in the hidden word you lose a life.""")
play_game = input("Would you like to play? (y/n)").lower().strip()

#Create game function


def run_game():
    lives_lost = 0
    letters_guessed = []
    if play_game == "y":
        print ("""

Selecting hidden word.....""")
        
        hidden_word = random.choice(words_list).upper()
        word_so_far = "*"*len(hidden_word)
        print(word_so_far)
        print("Please choose a letter. (Enter a letter between A-Z)")
        guess = input("Letter: ").upper().strip()

#Make sure guess is a string of 1 
        while len(guess)>1 or len(guess)<1 or guess.isdigit():
            guess = input ("Please enter one letter from the alphabet: ")
        if guess in hidden_word:
            letters_guessed.append(guess)
            print ("Well done! '" + guess + "' is in the hidden word!")
            new_word_so_far = ""
            for index, char in enumerate(hidden_word):
                if char == guess:
                    new_word_so_far += guess
                else:
                    new_word_so_far += word_so_far[index]
            word_so_far = new_word_so_far
            print(word_so_far)
            if word_so_far == hidden_word:
                print("You won! You guessed the word " + hidden_word + "!")
                return True
            else:
                print ("You have already guessed the letters: " + str(letters_guessed))
        else:
            print (guess + " is not in the hidden word - you lose a life!")
            lives_lost += 1
            print ("Lives left: " + (10-lives_lost))


run_game()



#Introduce the game to player and get player name - outline game rules:
#(10 failed guesses and game over)


            

    




#while loop - define function - if letter is in secret word, return word with correct guess inserted.
#if letter not in game, return fail message and update failed turns.
    #function to update failed guesses tracker - when ==0, game over
    #function to update secret word - when all letters guessed, You WIN
