# Assignment - 4


# Question - 1

# Marking scheme for grades
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A

# Input of his/her marks by user 
marks = float(input("Enter your marks :\n"))

# Code deciding grade of user according to marks scored
if 100 >= marks > 80:
    print("Your grade in the subject is : A")
elif 80>= marks >60 :
    print("Your grade in the subject is : B")
elif 60 >= marks >50 :
    print("Your grade in the subject is : C")
elif 50>= marks > 40 :
    print("Your grade in the subject is : D")
elif 40>= marks >= 25 :
    print("Your grade in the subject is : E")
# condition is marks are invalid 
elif marks > 100 or marks <= 0:
    print("Invalid Marks")
else:
    print("Your grade in the subject is : F")





# Question - 2

# Entry of year by user for checking leap year
year = int(input("Enter the yaer to be checked for leap yaer :\n"))

# Code to check if its divisible by 400 or not
if year % 400 == 0 :
    print("Yes, it is a leap year")

# Code to check if its divisible by 4 or not
# At the same time not divisible by 100

elif year % 4 == 0 and year % 100 != 0:
    print("Yes, it is a leap year")

# For rest of the cases as they are not leap year
else :
    print("No, it's not a leap year")





# Question - 3

# Importing ramdon as random is an in-built function
# randint function in random variable helps to select random numbers in the specified range

import random

# Taking turns to set while loop for number of questions
# As each time it runs new ques comes

turns = 0
n = 1
print()
# Asking user for number of questons in the test
ques = int(input("How many questions needed to be there in test :\n"))


# While loop helps us to go again and again and setting ques 
# This can make mny ques without typing them actually
while turns < ques:
    n_1 = random.randint(1,10)
    n_2 = random.randint(1,10)

    print()
    print("Q -",n)
    print("What is", n_1,"x",n_2 ,"?")

    answer = int(input("Enter your answer :\n"))

    if (n_1)*(n_2) == answer:
        print("Your given answer is Correct")
    else :
        print("Your given answer is Wrong")
    
    print("\n")

    # For making finite loop +1 is done
    turns = turns + 1
    n = n + 1




# Question - 4

for candies in range(0,200):
    if candies % 5 == 2:
        if candies % 6 == 3:
            if candies % 7 == 2:

                print(str(candies) + " is the correct answer")