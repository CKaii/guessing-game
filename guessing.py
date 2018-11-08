import random

random_number = random.randint(1,10)

msg = None

while msg != random_number:
    msg = input("guess a number between 1 and 10: ")
    msg = int(msg)
    if random_number == msg:
        print("You guessed it! You won!")
    elif msg > random_number:
        print("Too high, try again!")
    else:
        print("Too low, try again!")


