
'''

program20: write a program to find sum of natural numbers.

Output:

Enter the number = 16

sum = 136

'''

number = int(input("Enter any number: "))

y = 0

for x in range(1, number+1):
    y = x + y

print("sum of", number, "natural numbers is:",y )
