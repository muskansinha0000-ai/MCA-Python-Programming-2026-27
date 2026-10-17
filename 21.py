secret = 50

while True:
    guess = int(input("Guess the number:"))

    if guess>secret:
        print("Too high")
    elif guess<secret:
        print("Too low")
    else:
        print("You guesses it Right")
        break