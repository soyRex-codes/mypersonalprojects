import random

SIZE = 3
PLAYER_1_PIECE = 'O'
PLAYER_2_PIECE = 'X'

# Check if the current player has won
def check_win(table):
    # Check the rows
    for i in range(SIZE):
        if table[i][0] == table[i][1] == table[i][2] != ' ':
            return True

    # Check the columns
    for j in range(SIZE):
        if table[0][j] == table[1][j] == table[2][j] != ' ':
            return True

    # Check the diagonals
    if table[0][0] == table[1][1] == table[2][2] != ' ':
        return True
    if table[0][2] == table[1][1] == table[2][0] != ' ':
        return True

    return False

# Display the tic-tac-toe table
def display_table(table):
    for row in table:
        for cell in row:
            if cell == ' ':
                print("_ ", end='')
            else:
                print(f"{cell} ", end='')
        print()

# Check if the tic-tac-toe table is full
def check_table_full(table):
    for row in table:
        if ' ' in row:
            return False
    return True

# Check if the move made by player 1 is legal
def check_legal_option(table, row, col):
    if 0 <= row < SIZE and 0 <= col < SIZE and table[row][col] == ' ':
        return True
    return False

# Generate a move for player 2
def generate_player2_move(table):
    while True:
        row = random.randint(0, SIZE - 1)
        col = random.randint(0, SIZE - 1)
        if table[row][col] == ' ':
            table[row][col] = PLAYER_2_PIECE
            break

def main():
    print("The current state of the game is:")

    # Initialize the game board
    board = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

    # Seed the random number generator
    random.seed()

    game_over = False
    player1_turn = True

    while not game_over:
        # Display the current state of the game
        display_table(board)

        # Check if the game is over due to full table
        if check_table_full(board):
            print("Game over, no player wins.")
            game_over = True
            break

        if player1_turn:
            # Player 1's turn
            while True:
                try:
                    row, col = map(int, input("Player 1, enter your selection [row col]: ").split())
                    if check_legal_option(board, row - 1, col - 1):
                        board[row - 1][col - 1] = PLAYER_1_PIECE
                        break
                    else:
                        print("Invalid move. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter two integers separated by a space.")
        else:
            # Player 2's turn (AI)
            generate_player2_move(board)
            print("Player 2 has made a move.")

        # Check if the current player has won
        if check_win(board):
            display_table(board)
            if player1_turn:
                print("Congratulations, Player 1 wins!")
            else:
                print("Congratulations, Player 2 wins!")
            game_over = True
            break

        # Switch player
        player1_turn = not player1_turn

    print("Game over!")

if __name__ == "__main__":
    main()
