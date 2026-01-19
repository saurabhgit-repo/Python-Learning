print("Namaste Duniya ! I am Learning Python")

#Hello I am Saurabh how are you ? -- This is a single line comment

'''
This is a multi-line comment

'''

#Variables in Python

# In python variables are used as a storage to store things in python.

hero = "Saurabh"
hero1 = "Kumar"

age=12

# Special characters are not allowed in variable names except _ (underscore)

# Variables names should not start with numbers.
# Variables names are case sensitive.
# Variables names should not be the same as Python keywords.    
# Variables names should be meaningful.
# Variables names should not contain spaces. Use _ (underscore) instead of space.
# Variables can store different types of data like string, integer, float, boolean etc.

# Naming Conventions in Python

# Pascal Case : ShreyiansSchool="Students"
# Camel Case : shreyiansSchool="Students"
# Snake Case : shreyians_school="Students"

# Data Types in Python
# Data types are the things we store in variables and it defines what data type variables are.

a=12
print(type(a)) #integer data types

b= -34
print(type(a)) #integer data types

c=3.14
print(type(c)) #float data types

d=12/3
print(type(d)) #float data types

v= 34j #j denotes imaginary part of a complex number.
print(type(v))

s="Saurabh"
k='Kumar'  #Strings data types
print(type(s),type(k))

is_student=True
is_teacher=False  #Boolean data types
print(type(is_student),type(is_teacher))

a='A'
print(ord(a))  #ord() function gives the ASCII value of a character

b=65
print(chr(b)) #chr() function gives the character of a ASCII value

#Indexing in Python Strings

name="Saurabh"

print(name[0])
print(name[-1])

#String Slicing in Python

print(name[0:4]) #Slicing from index 0 to 3
print(name[0::2]) #Slicing from index 0 to end with a step of 2
print(name[::-1]) #Reversing a string using slicing

#Type Conversion in Python
a=12
print(type(a))

a=str(a)
print(type(a))

a="12"
a=int(a)
print(type(a))

a=0
print(bool(a))

a=52
print(bool(a))

#Implicit Type Conversion in Python
#Python automatically converts one data type to another data type.

a=12/3
print(a)
print(type(a))

#Input and Output in Python

print("Hello how are you ?")

name="Arya"
age=21
print(name,age)

#Formatted String
print(f"My name is {name} and my age is {age}")

#Input Function
name=input("Enter your name:")
print("Entered name is ",name)
print(type(name))

age=int(input("Enter your age:"))
print("Entered age is ",age)
print(type(age))

