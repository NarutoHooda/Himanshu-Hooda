#ques1
print("        Question-1")
x= int(input("Enter first number:\n "))
y= int(input("Enter second number:\n "))
z= int(input("Enter third number:\n "))
avg = (x + y + z)/3
print("The average of three numbers is: ", avg)


#ques2
print("        Question-2")
x = float(input("Enter your Gross income:\n$ "))
y= int(input("Enter number of dependents:\n "))
a = (x-10000-(3000*y))
b = a*0.20
print("income Tax is:\n$ ", b)


#program to store data in a list ques3
print("        Question-3")
print("[SID, Name, Gender, Course Name, CGPA]")
x  =  [ 21102015, "Himanshu Hooda", "M", "Civil Engineering", 9.8]
y  =  [ 21112115, "Himanshu", "M", "Civil Engineering", 8.8]
print(x)
print(y)


# sorting lists ques4
print("        Question-4")
x= [77, 75, 73, 78, 69]
x.sort()
print(x) 


#ques5(a)
print("        Question-5(a)")
Colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Colour.pop(3)
print(Colour)


#ques 5b
print("        Question-5(b)")
Colour = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
del Colour[3:5]
Colour.insert(3, "Purple")
print(Colour)
