import random

#numbers which are divisible by 7 and multiple of 5 - ex1

num_list = []
for x in range(1500, 2701):
    if(x%7 == 0 and x%5 == 0):
        num_list.append(str(x))
print(num_list)

#guess number - ex 2

number = random.randint(1,9)
guess = int(input("Enter a number : "))

while guess != number:
    guess = int(input("Try again : "))

else:
    print("Well guessed !! " )


#ex 3

val = 3
val_user = int(input("Enter 3 value :"))

if val == val_user:
    print("Hello !!")
else:
    print(" ")