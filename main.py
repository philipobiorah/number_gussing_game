import random
n = random.randrange(1,10)

guess = int(input("Enter any number: "))

while n!= guess:
    if guess < n:
        print("Too low")