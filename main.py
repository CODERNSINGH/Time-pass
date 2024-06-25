print("Welcome to my 2 digit Calculator: ")

a = int(input("Enter Your 1st Number: "))
b = int(input("Enter Your 2nd Number: "))

x = input("What task do you want to persform: ")

if x == "+":
    print("The Addition of These 2 is : " , a+b)
if x == "-":
    print("The Subtraction of These 2 is : " , a-b)
if x == "*":
    print("The Multiplication of These 2 is : " , a*b)
if x == "/":
    print("The Division of These 2 is : " , a/b)
