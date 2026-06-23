board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c]:
            return True
    return False

def board_full():
    for item in board:
        if item in "123456789":
            return False

    return True

display_board()

while True:
    # Player 1
    while True:
        try:
            position = int(input("Player 1 (X) Enter position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[position - 1] in "123456789":
                board[position - 1] = "X"
                break
            else:
                print("Position already occupied!")

        except ValueError:
            print("Please enter a valid number.")

    display_board()

    if check_winner():
        print("🎉 Player 1 (X) Wins!")
        break

    if board_full():
        print("🤝 Match Draw!")
        break

    # Player 2
    while True:
        try:
            position = int(input("Player 2 (O) Enter position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[position - 1] in "123456789":
                board[position - 1] = "O"
                break
            else:
                print("Position already occupied!")

        except ValueError:
            print("Please enter a valid number.")

    display_board()

    if check_winner():
        print("🎉 Player 2 (O) Wins!")
        break

    if board_full():
        print("🤝 Match Draw!")
        break