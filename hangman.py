#create list of words that will be randomly selected for the game
import random

words_list = ("TOMATO", "AVOCADO", "SAMPHIRE", "ASPARAGUS", "BROCCOLI", "CHICKPEA", "SHALLOTS", "WATERMELON", "SWEETCORN")

#Introduce game - would they like to play?
def introduction():
    print ("HELLO, AND WELCOME TO HANGMAN!")
    name = input("What is your name? ").strip()
    print ("Hello, " + name + "!")
    print ("The aim of the game is to guess the hidden word.\nYou have 10 lives - each time you guess a letter that is not in the hidden word you lose a life.")

def get_hidden_word():
    print ("\n\nSelecting hidden word.....\n\n")
    return random.choice(words_list).upper()

def end_game(hidden_word):
    print ("You have run out of lives -- GAME OVER -- ")
    print ("The hidden word was " + hidden_word + ". Better luck next time")
    play_again = input ("Would you like to play again? (y/n) ").lower().strip()
    if play_again == "y":
        run_game()
    else:
        print ("Goodbye! Have a great day!")

#Create game function

def run_game():
    introduction()
    hidden_word = get_hidden_word()


    word_so_far = "*"*len(hidden_word)
    print(word_so_far)
    lives_lost = 0
    total_letters_guessed = []
    while lives_lost<10:

        print("Please choose a letter. (Enter a letter between A-Z)")
        letter_guessed = input("Letter: ").upper().strip()

#Make sure guess is a string of 1 
        while len(letter_guessed)>1 or len(letter_guessed)<1 or letter_guessed.isdigit():
             letter_guessed = input ("Please enter one letter from the alphabet: ")
        total_letters_guessed.append(letter_guessed)
        if letter_guessed in hidden_word:
            print ("Well done! '" + letter_guessed + "' is in the hidden word!")
            new_word_so_far = ""
            for index, char in enumerate(hidden_word):
                if char == letter_guessed:
                    new_word_so_far += letter_guessed
                else:
                   new_word_so_far += word_so_far[index]
            word_so_far = new_word_so_far
            print(word_so_far)
            if word_so_far == hidden_word:
                print("You won! You guessed the word " + hidden_word + "!")
                play_again = input ("Would you like to play again? (y/n) ").lower().strip()
                if play_again == "y":
                    run_game()
                else:
                    print ("Goodbye! Have a great day!")
            else:
                print ("Letters already guessed: " + str(total_letters_guessed))
        else:
            print (letter_guessed + " is not in the hidden word - you lose a life!")
            lives_lost += 1
            print ("Lives left: " + str(10-int(lives_lost)))
            print ("Letters already guessed: " + str(total_letters_guessed))

        if lives_lost >=10:
            end_game(hidden_word)

run_game()

