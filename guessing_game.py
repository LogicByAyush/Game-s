import random
while True:

    print("\nWelcome to the Number Guessing Game!")
    move = 10
    level = input("Choose level (easy/medium/hard): ").lower()

    if level == "easy":
        secret = random.randint(1, 50)
        print("Guess the number between 1 to 50")
    elif level == "medium":
        secret = random.randint(1, 100)
        print("Guess the number between 1 to 100")
    elif level == "hard":
        secret = random.randint(1, 500)
        print("Guess the number between 1 to 500")
    else:
        print("Invalid level!")
        continue

    while move > 0:
        guess = int(input(f"\nYou have {move} moves remaining.\nEnter your guess: "))

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("🎉 Congratulations! You guessed it.")
            break

        move -= 1

    if move == 0:
        print(f"😢 You Lost!! The number was {secret}")

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break