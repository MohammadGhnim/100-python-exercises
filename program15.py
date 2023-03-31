

'''

Program15: Write a program to find most frequent number from list or array.

Output:

list1 = [2,,3,4,5,2,4,2,5,2,8]

most frequent number = 2

'''

from statistics import mode

list1 = [2,3,4,5,2,4,2,5,2,8]

most_frequent_number = mode(list1)

print("Most Frequent Number is: ", most_frequent_number)
