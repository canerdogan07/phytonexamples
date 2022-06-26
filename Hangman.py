##Hangman Challenge

import random
import sys
from time import sleep

#Variables

keyword_list = ["piano","hotel","screw","snake","final","red"]
guessed_word = []
secret_word = random.choice(keyword_list)
word_length = len(secret_word)
alphabeth = "abcdefghijklmnopqrstuvwxyz"
guessed_letters = []

def rules():
    for letter in secret_word:
        guessed_word.append("-")
    print("The word contains ", word_length, "letters.")
    sleep(3)
    print("You have 10 guesses.")
    sleep(3)
    print("If you fail to guess 10 times, you will lose.")
    sleep(3)
    print(guessed_word)

def wordprediction():
    while True:
        prediction = input("Would you like to guess the word? You will lose if your prediction is wrong.\n")
        if prediction == "Yes":
            predictiontest = input("Guess the word.\n")
            if predictiontest == secret_word:
                print("Congrats, you are correct.")
                sys.exit()
            else:
                print("Your guess is wrong. Game Over!")
                sleep(3)
                print("The word was", secret_word)
                sys.exit()
        elif (prediction == "No"):
            print("Continue the game.\n")
            break
        else:
            print("Please type Yes or No\n")
            continue

def guess_count():
    guessnumber = 0
    while guessnumber < 10:
        wordprediction()
        tryletter = input("Please try a letter.\n")
        if not tryletter in alphabeth:
            print("Please use the alphabeth.")
        elif tryletter in guessed_letters:
            print("You have already guessed that letter.\n")
        else:
            guessed_letters.append(tryletter)
        if tryletter in secret_word:
            print("Correct!")
            for x in range(0,word_length):
                if secret_word[x] == tryletter:
                    guessed_word[x] = tryletter
                print(guessed_word)
                if not "-" in guessed_word:
                    print("You have won!")
                    break
        else:
            print("Wrong guess. You have", 10 - guessnumber, "tries left. Try again.\n")
            guessnumber += 1
        if guessnumber==10:
            print("Game over. The word was", secret_word)
rules()
guess_count()

