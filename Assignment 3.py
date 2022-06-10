# Assignment - 3



# Question - 1

# Program to convert a number into it's binary equivalent

# Input of number to be converted by user
number = int(input(("Enter the number whose binary is to calculated :\n")))

# Number being converted into binary using inbuilt function
binary = bin(number)

# Printing the binary to the number entered
print("Binary of the number entered is :",binary[2:])



# Question - 2

# 1st Input of number by user
first_number = float(input('Enter first number:\n '))

# Asking user for the operator to be used 
operator = input('Enter operation(+, -, *, / or quit to end calculator):\n ')

# Calculation part of the code asking further enteries
# Using while and if
while (operator != 'quit'):
    if operator == '+':
        first_number = first_number + float(input('Next number:\n '))
    elif operator == '-':
        first_number = first_number - float(input('Next number:\n '))
    elif operator == '*':
        first_number = first_number * float(input('Next number:\n '))
    elif operator == '/':
        first_number = first_number / float(input('Next number:\n '))
    else:
        print('Invalid operator, try again')
    operator = input('Enter operation(+, -, *, / or quit to end calculator):\n ')

print(first_number)



# Question - 3

import math


# Code for 1st expression
exp1 = (3+4) * (5)
print(exp1)

# Code for 2nd expresion 
# Asking user for the value of n at which the expression is to be solved
n = float(input("Enter value of n for (n)(n-1))/2 :\n"))
exp2 = ((n)*(n-1)) / 2 
print(exp2)



# Code for 3rd expression 
# Asking user for the value of r at which the expression is to be solved
r = float(input("Enter value of r for 3rd expression :\n"))
exp3 = 4*(math.pi) * (math.pow(r,2))
print(exp3)



# Code for 4th expression
# Asking user for the value of r,α and β at which the expression is to be solved
r = float(input("Enter value of r for 4th expression :\n"))
α = float(input("Enter value of α for 4th expression :\n"))
β = float(input("Enter value of β for 4th expression :\n"))
exp4 = math.sqrt(r*(math.pow(math.cos(α), 2)) + r*(math.pow(math.sin(β), 2)))
print(exp4)



# Code for 5th expression
# Asking user for the value of y1,y2,x1 and x2 at which the expression is to be solved
y1 = float(input("Enter value of y1 for 5th expression :\n"))
y2 = float(input("Enter value of y2 for 5th expression :\n"))
x1 = float(input("Enter value of x1 for 5th expression :\n"))
x2 = float(input("Enter value of x2 for 5th expression :\n"))
exp5 = (y2 - y1)/(x2 - x1)
print(exp5)




# Question - 4


# Part-a)
for i in range(5):
    print(i, end=" ")
print()
print()

# Part-b)
for i in range(3,10):
    print(i, end=" ")
print()
print()

# Part-c)
for i in range(4,13,3):
    print(i, end=" ")
print()
print()

# Part-d)
for i in range(15,5,-2):
    print(i, end=" ")
print()
print()

# Part-e)
for i in range(5,3):
    print(i, end=" ")



# Question - 5

# Code to find the molecular weight of a compund
# Compound contains Hydrogen, Carbon and Oxygen atoms

# Input by user on number of Hydrogen atom(H-atom)
No_H = int(input('Enter number of Hydrogen Atoms: \n'))

# Input by user on number of Carbon atom(C-atom)
No_C = int(input('Enter number of Carbon Atoms: \n'))

# Input by user on number of Oxygen atom(O-atom)
No_O = int(input('Enter number of Oxygen Atoms: \n'))

# Sum of all the atoms i.e. total molecular mass of the molecule
total_molecular_mass = (No_H * 1.00794) + (No_C * 12.0107) + (No_O * 15.9994)
print('Molecular weight of compound is:', total_molecular_mass , 'grams/mole')