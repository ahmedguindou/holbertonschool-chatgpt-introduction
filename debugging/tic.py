def print_board(board):
    """
    Prints the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Checks if there is a winner.
    Returns True if a player has won, otherwise False.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_draw(board):
    """
    Checks if the board is full and there is no winner (a draw).
    Returns True if it's a draw, otherwise False.
    """
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            # Prompt user input
            row = input(f"Enter row (0, 1, or 2) for player {player}: ").strip()
            col = input(f"Enter column (0, 1, or 2) for player {player}: ").strip()

            # Validate input
            if not row.isdigit() or not col.isdigit():
                print("Invalid input! Please enter numbers only.")
                continue

            row, col = int(row), int(col)

            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be between 0 and 2.")
                continue

            # Check if spot is already taken
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Place the player's mark
            board[row][col] = player

            # Check for a winner
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Check for a draw
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            player = "O" if player == "X" else "X"

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


if __name__ == "__main__":
    tic_tac_toe()