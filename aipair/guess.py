import random

number = random.randint(1, 15)

attempts = 0
while attempts < 3:
    try:
        guess = int(input("Guess a number from 1 to 15: "))
    except ValueError:
        print("Please enter a whole number.")
        continue
    except EOFError:
        print("Input ended. Better luck next time!")
        break

    if not 1 <= guess <= 15:
        print("Please choose a number between 1 and 15.")
        continue

    attempts += 1

    if guess == number:
        print("You guessed it!")
        break
else:
    print("Out of attempts. Better luck next time!")

    