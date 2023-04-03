
'''
program21: Write a program to find LCM-

Output:

Enter the number1 = 54
Enter the number2 = 24

L.C.M = 216

'''

def find_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

        
    while(True):
        if((greater %x == 0)and (greater %y == 0)):
            lcm = greater
            break
        greater += 1
        
    return lcm

num1 = 54
num2 = 24

print("LCM of numbers is: ", find_lcm(num1, num2))
