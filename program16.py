
'''

program16: Write a program to find area of triangle.


Output:

a = 5
b = 6
c = 7

The area of triangle is 14.70


'''

a = 5
b = 6
c = 7

#semi perimeter:

s = (a + b + c) / 2


#area:

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("The area of the triangle is: ", area)
