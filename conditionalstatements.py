#Conditional Statements in Python:
#if Statement
a=13
if a>10:
    print("Task A")

#if-else Statement
a=13
if a>10:
    print("Task A")
else:
    print("Task B")

money=int(input("Please provide me money"))
if money==10:
    print("I will have a choco-bar ice-cream")

elif money>10:
    print(" I will have a vanilla ice-cream")
else:
    print("Chocolate")

#1.Accept two numbers and print the greatest number
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if num1>num2:
    print(f"{num1}is greater than {num2}")

elif num2>num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")

#2.Accept the gender from the user as char and print the respective greeting message
#Ex- Good morning sir/ma'am

gender=input("Enter Male or female(M/F):")
if(gender=='M' or gender=='m'):
    print("Good morning sir")
elif(gender=='F' or gender=='f'):
    print("Good morning ma'am")
else:
    print("Invalid Input")

#3.Accept an integer and check whether it is even or odd
num=int(input("Enter an integer :"))
if(num%2==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#4. Accept name and age from the user and check whether it is valid user or not
name=input("Enter your name:")
age=int(input("Enter your age:"))

if(age>=18):
    print(f"Hello {name} you are eligible to vote")
else:
    print("You are not eligible to vote")

#5.Accept a year and check whether it is a leap year or not
year=int(input("Enter a year:"))
if(year%4==0) and (year%100!=0):
    print(f"{year} is a leap year")
elif(year%100==0) and (year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#if-elif ladder
t=int(input("Please tell your temperature:"))
if t<0:
    print('Freezing cold')
elif t>=0 and t<10:
    print("Very Cold")
elif t>=10 and t<20:
    print("Cold")
elif t>=20 and t<30:
    print("Pleasant")
elif t>=30 and t<40:
    print("Hot")
elif t>=40 and t<50:
    print("Very Hot")