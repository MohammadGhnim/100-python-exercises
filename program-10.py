
'''

program10: Write a program to find a factorial of any given number.

Output:

number = 5
factorial = 5*4*3*2*1 = 120

number = 4
factorial = 4*3*2*1 = 24



'''
#Method1:


number = int(input("Enter any number: "))
fact = 1

for x in range(1, number+1):
    fact = fact * x

print("Factorial of", number, "is:", fact)


print('--------------------------------')


#Method2:

import math

number = int(input("Enter any number: "))

print("Factorial of", number, "is:", math.factorial(number))

