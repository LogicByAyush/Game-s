import random

choices = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}


def get_player_choice():
    while True:
        choice = input("\nR for Rock\nP for Paper\nS for Scissors\nEnter your choice: ").lower()

        if choice in choices:
            return choice

        print("Invalid choice! Please enter R, P, or S.")


def get_computer_choice():
    return random.choice(["r", "p", "s"])


def check_winner(player, computer):
    if player == computer:
        return "draw"

    if (
        (player == "r" and computer == "s")
        or (player == "p" and computer == "r")
        or (player == "s" and computer == "p")
    ):
        return "player"

    return "computer"


player_name = input("Enter your name: ")

player_score = 0
computer_score = 0

print("\n===== BEST OF 5 =====")

for round_num in range(1, 6):
    print(f"\n----- Round {round_num} -----")

    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f"\n{player_name} chose: {choices[player_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    result = check_winner(player_choice, computer_choice)

    if result == "player":
        print(f"{player_name} Wins This Round!")
        player_score += 1

    elif result == "computer":
        print("Computer Wins This Round!")
        computer_score += 1

    else:
        print("Round Draw!")

    print(f"\nScore:")
    print(f"{player_name}: {player_score}")
    print(f"Computer: {computer_score}")

print("\n===== FINAL RESULT =====")

if player_score > computer_score:
    print(f"🏆 Congratulations {player_name}! You Won The Match!")

elif computer_score > player_score:
    print("🏆 Computer Won The Match!")

else:
    print("🤝 Match Draw!")