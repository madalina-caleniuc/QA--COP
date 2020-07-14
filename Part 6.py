
# ex1 -the sum of n numbers from user input

print("Ex 1")
n_numbers = input("Enter numbers separated by space ")
numberList = n_numbers.split()

print("All entered numbers ", numberList)

def sum_list():
    sum1 = 0
    for num in numberList:
        sum1 += int(num)
    print("Sum of all entered numbers = ", sum1)

sum_list()

print('\n')

#ex 2 - new list of only the first and last elements of the given list

print("Ex 2")

a_list = [5, 10, 15, 20, 25]
print("The original list is :  " + str(a_list))

def take_numbers():
    new_list = [a_list[0], a_list[-1]]
    print("Fist and last elements are :" + str(new_list))

take_numbers()

print('\n')

#ex 3 - Fibonacci numbers

print("Ex 3")

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("How many Fibonacci numbers do you want ? "))

if nterms <= 0:
   print("Plese enter a positive number !!")
else:
   print("The Fibonacci sequence generated is :")
   for i in range(nterms):
       print(recur_fibo(i))

print('\n')

#ex 4 - execute a string containing Python code

print("Ex 4")

s_code = "7 + 3"
string_code = """

numbers = [2, 3, 4, 5,6]
new_numbers = [numbers[0], numbers[-1]]
print(new_numbers)

"""

exec(string_code)
print(eval(s_code))