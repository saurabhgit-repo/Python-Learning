# Loops in Python:

#1. For Loop:
#range(start,stop,step) (s,s,s)

a=range(1,20,1)

for i in a:
    print(i) # It return 1 to 19 --20 will not be included

for i in range(1,21):
    print(i)

for i in range(11): #Automatically starts from 0 
    print(i)

for i in range(20,51): #It will print from 20 to 50
    print(i)

for i in range(16,0,-1): #It will print from 16 to 1
    print(i)

for i in range(-5,-16,-1): #It will print from -5 to -15
    print(i)

#Lets print a table of 5:
for i in range(5,51,5):
    print(i)

#n=int(input("Enter a number table you want: "))

#for i in range(n,(n*10)+1,n):
    print(i)

#Loops for string:
#1.With indexinG:
a="Saurabh"
for i in range(0,7):
    print(a[i])

for i in range(len(a)):
    print(a[i])

#2. Directly over the string:
b="MIT MEERUT"

for i in b:
    print(i)

#break statement:
for i in range(1,21):
    if i==15:
        break
    else:
        print(i)

#Continue statement:
for i in range(1,21):
    if i==15:
        continue
    print(i)

#Else with for loop:
for i in range(1,21):
    if i==15:
        print("Break statement is executed")
        break
    print(i)
else:
    print("Break statement is not executed")