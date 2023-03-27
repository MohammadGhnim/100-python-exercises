
'''

Program9: Write a program to check number whether it is prime or not.


Output:

number = 6
It is not prime

number = 7
It is prime


'''

# Logic: divide number from 2 to that number and count reminder if it equals to 0.

number = 102
counter = 0

for x in range(2, number):
    if (number % x == 0):
        counter = counter + 1

        
if (counter == 0):
    print("It is prime number")
else:
    print("It is not prime number")
