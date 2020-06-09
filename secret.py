import random

secret = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == secret:
        print("OK")
        break
    elif guess < secret:
        print("Your guess was too low!")
    else:
        print("Your guess was too high!")