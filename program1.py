#Program 1: Write a program which print "Hello World"
#Output: Hello World

#Solution:
print("Hello World")




'''

Python print() Function:

- Definition and Usage:

The print() function prints the specified message to the screen, or other standard output device.

The message can be a string, or any other object, the object will be converted into a string before written to the screen.


- Syntax:

print(object(s), sep=separator, end=end, file=file, flush=flush)


- Parameter Values:

1- object(s): Any object, and as many as you like. Will be converted to string before printed

2- sep='separator': Optional. Specify how to separate the objects, if there is more than one. Default is ' '

3- end='end': Optional. Specify what to print at the end. Default is '\n' (line feed)

4- file: Optional. An object with a write method. Default is sys.stdout

5- flush: Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False

'''

#More Examples:

#1- Print a tuple:

x = ("apple", "banana", "cherry")
print(x)
#>>> ('apple', 'banana', 'cherry')


#2- Print two messages, and specify the separator:

print("Hello", "how are you?", sep="---")
#>>> Hello---how are you?


