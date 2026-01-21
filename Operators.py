#Operators in Python
#Arithmetic Operators in Python:
a=12
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

print(12+4/2)

#Assignment Operators in Python:
a=5
print(a)

a+=3
print(a)

#Compound Assignment Operators in Python:
a=20
a+=20 #Reassigns a with a+20
a+=30 #Reassigns a with a+30
a+=40 #Reassigns a with a+40
print(a)


#Comparison Operators in Python:
a=10
b=20
print(a==b) #Double equal to operator
print(a!=b) #Not equal to operator
print(a>b) #Greater than operator
print(a<b) #Less than operator
print(a>=b) #Greater than equal to operator
print(a<=b) #Less than equal to operator

print(ord('A'))
print(ord('a'))

print("A">"a") #False because ASCII value of 'A' is 65 and 'a' is 97

print("ABC">"ACD") #False because 'B' comes before 'C' in ASCII table

#print('A'>32) #cannot compare string with integer, gives error

#Logical Operators in Python:

print(123>100 and 123<200 and 45==90) # It returns False as one condition is False

print(123>100 or 123<200) #One condition is True, so returns True

print(not(123>100)) #It returns False as 123>100 is True and not operator negates it

print(126>130) #False
print(456==456)!=(235==236) #True
print(12<10 or 45==56 or 69>70 or 15!=13) #False or False or False or True = True
print(True and bool(0)) #False because bool(0) is False
