# Basic python Installation

# First Test Code 
msg="Hello World!!"
print(msg)

# Second Test code to read name , age to check voting eligiblity 
nm=input("Enter your name : ")
age=int(input("Enter your age :"))

if age>=18:
    print(nm, "You are eligible to vote:")
else:
    print(nm,"You are not eligible to vote")


# Read 3 no from the users to determine the greatest among the three

a= int(input("Enter First no "))
b= int(input("Enter Second no "))
c= int(input("Enter Third no "))

# Comparing for the greatest no 

if a>b and a>c :
    print(a, "is greatest ")
if b>a and b>c :
     print(b, "is greatest")
if c>a and c>b :
    print(c, "is greatest")        