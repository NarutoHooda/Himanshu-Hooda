# Assignment - 5



# Question - 1

# print() creates a space inbetween lines while execution of codes making them easier to read
print()
# Input by user of the string needed to be reversed
string = str(input("Enter the string to be printed in reverse order :\n"))

# Another string equals to the inverted of the main input string 
string1 = string[::-1]

print()

# Code to print the reversed oredered string
print("The reversed order of string entered is :")
print(string1)
print()



# Question - 2

# print() creates a space inbetween lines while execution of codes making them easier to read
print()
range_1 = int(input("Enter the initial number of range :\n"))
print()
range_2 = int(input("Enter the last(ending) number of range :\n"))
print()
a = 1
number = int(input("Enter the divisor for entered range :\n"))

print()

print("Numbers divisile in the range are :")

for i in range(range_1,range_2):
    if i % number == 0:
        print(a,")",i)
        print()
    else:
        continue
    a = a + 1 



# Question - 3

import math

# print() creates a space inbetween lines while execution of codes making them easier to read
# making them more clear annd easy to read

print()

# Input by user of different sides of triangle

side_1 = float(input("Enter the lenght of 1st side of triangle whose area is to be calculated :\n"))
print()
side_2 = float(input("Enter the lenght of 2nd side of triangle whose area is to be calculated :\n"))
print()
side_3 = float(input("Enter the lenght of 3rd side of triangle whose area is to be calculated :\n"))
print()

s = (side_1+side_2+side_3)/2

largest  = max(side_1,side_2,side_3)

# Largest for checking if the given sieds of triangle are even possible 
# s can't be less than any side as -ve sqrt is not defined

if s > side_3 and s> side_1 and side_2 < s and largest < ((side_1 + side_2 + side_3) - largest):
    print("Area of triangle whose sides are entered is :" , 
    math.sqrt( s*(s-side_1)*(s-side_2)*(s-side_3) ))
    
else:
    print("Triangle not possible")

print()



# Question - 4

# i will deicide the number of rows of * be printed
# n will deicded the number of times * be printed

i = 0
n = 0 
x = "*"

# print() creates a space inbetween lines while execution of codes making them easier to read
print()

while i <=9:
    while n <= 5:
        print(n*x)
        n = n + 1
        i = i + 1

    while i <= 9 : 
        print((n-2)*x)
        n = n - 1
        i = i + 1

print()




# Question - 5

# rows takes input on number of rows of alphabets to be printed making right angled triangle
# a determines which alphabet to be printed next 
# 2nd loop i.e. j detemines the columns of triangle(pattern)

# print() creates a space inbetween lines while execution of codes making them easier to read
print()

rows = int(input("Enter number of rows to be printed :\n"))
print()
a = 0

print("The pattern obtained with rows equals to",rows,"is:")
for i in range (rows) :
    for j in range(i+1):
        print((chr(65+a)),end = "")
        a = a + 1

# while helps to set radar over captial alphabets only
        while a > 25:
            a = a - 26
    print()

print()



# Question - 6

# First, we will take the input: 
# The upper value and lower value of range 
print()
lower_value = int(input ("Please, Enter the Lowest Range Value : \n"))  
upper_value = int(input ("Please, Enter the Upper Range Value : \n"))  

# Prime numbers are whose who only are divisible by :
# number 1 and themselves

a = 1

# print() creates a space inbetween lines while execution of codes making them easier to read
print()

print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (a,")",number)  
            a += 1

print()



# Question - 7

# Making 3 different loops for 3 cases of divisibility

# print() creates a space inbetween lines while execution of codes making them easier to read
print()
# Case - 1 : only divisible by "7"
print("The numbers are divisible by only 7 not 11:")
for i in range(1,500):
    if i % 7 == 0 and i % 11 != 0:
        print(i)


print()
# Case - 2 : only divisible by "11"
print("The numbers are only divisible by only 11 not 7:")
for i in range(1,500):

    if i % 7 != 0 and i % 11 == 0:
        print(i)


print()
# Case - 3 : divisible by both "7" and "11"
print("The numbers are divisible by both 7 and 11:")
for i in range(1,500):

    if i % 7 == 0 and i % 11 == 0:
        print(i)
print()




# Question - 8

# list_p is a list containg all the positive numbers
# list_n is a list containg all the negative numbers
# list_o is a list containg all the odd numbers
# list_e is a list containg all the even numbers

list_p = []
list_n = []
list_o = []
list_e = []

# print() creates a space inbetween lines while execution of codes making them easier to read
print()

# Input of 10 different numbers by the user of his choice

num_1 =  int(input("Enter the 1st number to be checked :\n"))
num_2 =  int(input("Enter the 2nd number to be checked :\n"))
num_3 =  int(input("Enter the 3rd number to be checked :\n"))
num_4 =  int(input("Enter the 4th number to be checked :\n"))
num_5 =  int(input("Enter the 5th number to be checked :\n"))
num_6 =  int(input("Enter the 6th number to be checked :\n"))
num_7 =  int(input("Enter the 7th number to be checked :\n"))
num_8 =  int(input("Enter the 8th number to be checked :\n"))
num_9 =  int(input("Enter the 9th number to be checked :\n"))
num_10= int(input("Enter the 10th number to be checked :\n"))

# list_all contains all the 10 numbers uploaded by user

list_all = [num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9,num_10]

print()

# a helps in providing sequence to result
a = 1
for i in list_all:
# For checking of number to be positive or negative:
# According to their types it is added to that particular list
    if i >= 0 :
        print(a,")",i,"is a positive ", end = "")
        list_p.append(i)
    else:
        list_n.append(i)
        print(a,")",i,"is a negative ", end="")
    a +=1

# For checking of number to be even or odd:
# According to their types it is added to that particular list
    if i % 2 == 0:
        list_e.append(i)
        print("as well as even number.")
    else:
        list_o.append(i)
        print("as well as odd number")
    
    print()

# Different lists are printed according to number's types

print("The following input numbers are odd :\n",*list_o , sep = " , ")
print()
print("The following input numbers are positive :\n",*list_p , sep = " , ")
print()
print("The following input numbers are negative :\n",*list_n , sep = " , ")
print()
print("The following input numbers are even :\n",*list_e , sep = " , ")
print()

# Part - e : Count of number of appearences

Number = int(input("Enter the number whose appearences are to be couted :\n"))
count_1 = list_all.count(Number)
print()
print("The number",Number,"appeared",count_1,"times.")
print()




# Question - 9

# Input of string by user 
line_1 = input("Enter the string :\n")

# Creating an empty dictonary to store all different words
count_1 = dict()

# Storing all words in a list by seprating them
words = line_1.split(' ')
for word in words :
    if word in count_1 :
        count_1[word] += 1
    else :
        count_1[word] = 1

print(count_1)



print("Thank you. \nYou have run all the codes and reached end of the assignment.")