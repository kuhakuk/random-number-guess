import random

def guess(x):
    random_number = random.randint(2, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Guess too low")
        elif guess > random_number:
            print("Guess too high")

    print(f"You have gueesed the right number {random_number}!!!")


guess(10)
 