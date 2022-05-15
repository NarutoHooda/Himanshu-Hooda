# Question-6
 
from itertools import count


print()

a = int(input("Enter 1st number :\n"))
print()
b = int(input("Enter 2nd number :\n"))
print()
num = a^b
count = 0
while (num!=0):
    num = num&(num - 1)
    count + 1
print("Number of bits needed to be flipped to convert a to b is :\n" , count)
print()
