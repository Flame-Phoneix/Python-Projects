from random import randrange

n = randrange(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess==n:
            print("Congratulations! You guessed the number.")
            break
        elif guess> n:
            print("Too high!") 
        elif guess<n:
            print("Too low!")
        else:
            print("Please enter a valid number")
    except ValueError:
        print("Please enter a valid number")