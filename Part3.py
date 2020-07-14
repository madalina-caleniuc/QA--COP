from __future__ import print_function
import random

#ex1 - program for user counting - ex 1
print("Ex 1")

#starting_num = input("enter the starting number :")
#ending_num = input("enter the ending number :")
#count_amount = input("enter the count amount")
#for si range
#daca range startul este > ending ?
#count negativ/pozitiv start/end > si <

starting_num = int(input("enter the starting number : "))
ending_num = int(input("enter the ending number :"))
count_amount = int(input("enter the count amount"))

for x in range(starting_num, ending_num, count_amount):
    print(x)

print('\n')

#ex2 - message from the user
print("Ex 2")

input_mess = input("Enter name : ")
print(input_mess[::-1])
print('\n')

#ex 3 - guess the word
#random pe lista data
#cu lenght pt determinarea nr de caractere din cuvant
#un for cu range pt nr de sanse
#citirea literei
#verificare daca apartine cuvantului
#yes sau no raspuns pt user
#input for word

print("Ex 3")

list_words = ["pizza", "apple"]
word = random.choice(list_words)
print("The number of letters : " + str(len(word)))

guesses = []

max_try = 5

while max_try > 0:
    failed = 0
    for char in word:
        if char in guesses:
           print(char)

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win")
        print("The word is ", word)
        break

    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        max_try -= 1
        print("wrong")

        print("You have " + str(max_try) + " chances")

        if max_try == 0:
                print("You loose")


#ex 4 - Write a Python program to construct the following pattern

#- 2 x for loop -> crescator si descrescator
#this is not complete

print("Ex 4")

r = range(1,4)

for i in r:
    for j in range(i):
        print ('* ', end="")
    print('')

for i in reversed(r):
    for j in range(i):
        print('* ', end="")
    print('')



