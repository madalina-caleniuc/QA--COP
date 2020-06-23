from __future__ import print_function
import random

# Part 3

# guess the word - ex 3

def get_random_word():
    words = ["pizza", "pizza"]
    word = words[random.randint(0, len(words)-1)]
    return word

def show_word(word):
    for character in word:
        print(character, " ", end=" " )
    print(" ")

def get_guess():
    print("Enter a letter :")
    return input()

def play_word_game():
    strikes = 0
    max_strikes = 5
    playing = True

    word = get_random_word()
    blanked_word = "_" * len(word)

    while playing:
        show_word(blanked_word)
        letter = get_guess()

        strikes += 1

        if strikes >= max_strikes:
            playing = False

    if strikes >= max_strikes:
        print("game over")
    else:
        print("winner")

print("Game starting...")
get_random_word()
play_word_game()
print("Game Finished")







