import random

#ex 1 - numbers which are divisible by 7 and multiple of 5
print('Ex 1')

for x in range(1500, 2701):
    if(x%7 == 0 and x%5 == 0):
        print(x)

# ex 2 guess a number between 1 to 9.
#din documt de cautat chiar daca introduc string sa nu imi dea eroare
print('Ex 2')

number = random.randint(1,9)
guess = int(input("Enter a number : "))

while guess != number:
    try:
        guess = int(input("Try again : "))
    except ValueError:
        print("It must be a number")

else:
    print("Well guessed !! " )

#ex 3 - print messages on the screen as long as a condition is met.
print("Ex 3")

value = input("Please enter '1'- Continue program or '2'-Exit : ")
num = 50

if value == "1":
    newnum = int(input("Enter a number:"))
    while newnum < num:
        print(newnum)
        newnum += 1
if value == "2":
    print(("Exit"))
else:
    print("Please run again and enter '1'- exit' or '2'- continue :")



