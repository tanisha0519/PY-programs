import random
secret_number = random.randint(1, 100)
print("===== NUMBER GUESSING GAME =====")
print("I have chosen a number between 1 and 100.")
print("Try to guess it!")
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too Low! Try Again.")
    elif guess > secret_number:
        print("Too High! Try Again.")
    else:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print("Number =", secret_number)
        print("Attempts =", attempts)
        break