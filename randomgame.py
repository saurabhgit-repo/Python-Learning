# Create a random number guessing game with python :

import random

num=random.randint(1,10)
tries=0

while True:
    guess=int(input("Please guess your number b/w 1 and 10"))

    if num==guess:
        tries=tries+1
        print(f"You are right you guessed the number in {tries} tries")
        break
    elif num<guess:
        tries=tries+1
        print("Go a little lower")
    elif num>guess:
        tries=tries+1
        print("Go to little higher")
    else:
        tries=tries+1
        print("Sorry you are wrong")

