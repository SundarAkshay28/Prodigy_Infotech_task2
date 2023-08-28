import random
secret_number = random.randint(1, 50)
attempts = 0
guess = None
print("")
while guess != secret_number:
    try:
        guess = int(input("Guess the number between 1 and 50: "))
        attempts += 1
        if guess < secret_number:
            print("Guess Higher!")
        elif guess > secret_number:
            print("Guess Lower!")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
    except ValueError:
        print("Please enter a valid number.")

print("Thanks for playing!")
