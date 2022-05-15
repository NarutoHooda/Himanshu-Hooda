# Question-5

print()

a = int(input("Enter length of 1st side\n"))
b = int(input("Enter length of 2nd side\n"))  
c = int(input("Enter length of 3rd side\n"))

print()

print("Will the sides form a triangle:" , end = " ")
if (a+b) < c or (a+c) < b or (b+c) < a:
    print("No")
else:
        print("Yes")
print()