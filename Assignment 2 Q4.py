# Question-4
from unicodedata import name


print()

a = str(input("Enter the statement\n"))
print()
print('''Is "name" present in the statement entered by user:''' , end=" " )
if "name" in a:
    print("Yes")
else:
    print("No")    
