# Assignment-2

# Question-1

from audioop import reverse
print()
print()


Q_1 = "Python is a case sensitive language"

# Part a 
print("The length of the string is :\n" , len(Q_1))

print()


# Part b
print("The string in reversed order :\n" , Q_1[::-1])

print()

# Part c
print("New string :\n" , Q_1[10:26])

print()

# Part d
print("The new replaced string is :\n" , Q_1.replace("a case sensitive" , "object oriented"))
print()

# Part e 
print('''The index of substrig a is :\n''' , Q_1.find("a"))
print()

# Part f
print("After removing the spaces string becomes:\n" , Q_1.replace(" " , ""))
print()
