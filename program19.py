

'''

program19: Write a program to check leap year.
(leap year = السنة الكبيسة)


Output:

Enter the year = 2011
It's not leap year

Enter the year = 2000
It's leap year


'''


import calendar

year = int(input("Enter year: "))

if (calendar.isleap(year)):
    print(year, " is leap year")
else:
    print(year, "is not leap year")
