

'''

program14: Write a program that switches the values stored in the variables a and b.

'''


#Method 1:
a = input("a: ")
b = input("b: ")

a, b = b, a

print("a: " + a)
print("b: " + b)


print("-------------------------")
#method 2:

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

