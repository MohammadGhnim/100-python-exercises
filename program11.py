

'''

Program11: Write a program to find ASCII value of character.


Output:

character = a
assci = 97

Note: ASCII (American Standard Code for Information Interchange)
 is the most common character encoding format for text data in computers and on the internet.
 In standard ASCII-encoded data, there are unique values for 128 alphabetic,
 numeric or special additional characters and control codes.


'''

character = str(input("Enter any character: "))

ASCII_CODE = ord(character)

print('ASCII Code of', character, "is: ", ASCII_CODE)
