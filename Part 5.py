import random

# ex 1 - list of random words
print("Ex 1")
print('\n')

words = ["apple", "orange", "kiwi"]
random.shuffle(words)
print(words)

print('\n')

#ex 2
print('Ex 2')

list_a = [1,6,8,9,6.7,1.1]
print(sum(list_a))
print('\n')

#ex 3 & 4- Who's your daddy ?
#this isn't complete
print('Ex 3&4')

fathers_names = {"alex":"Jonny Bravo", "tom":"Aladin Aka", "chris":"unkown"}
options = input("Choose an option: 0)Search son-father pair 1)Add son-father pair 2)Delete son-father pair 3) Replace son-father pair :")

if options == "0":
    input_name = input("Enter your name : ")
    if input_name in fathers_names:
        print((input_name) + " is the son of " + (fathers_names[input_name]))
    else:
        print("name is not in the list")

if options == "1":
    new_father = input("Enter new father name: ")
    new_son = input("Enter new son name :")
    fathers_names[new_father] = new_son
    fathers_names.__setitem__(new_father,new_son)
    print(str(fathers_names))

if options == "2":
    for i in fathers_names:
        print(fathers_names[i])
    delete_input = input(("Enter the name you want to delete : "))
    if delete_input in fathers_names:
        del fathers_names[delete_input]
        print(fathers_names)
    else:
        print("name not in the list")
