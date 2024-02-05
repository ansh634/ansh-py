EMPTY = "-"
board = [EMPTY] * 9
current_player = 'X'

def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

def player_input():
    while True:
        print(f"Player {current_player}'s turn")
        try:
            inp = int(input("Select a spot 1-9: "))
            if 1 <= inp <= 9 and board[inp-1] == EMPTY:
                return inp - 1
            else:
                print("Invalid input or spot already filled")
        except ValueError:
            print("Invalid input, please enter a number")


def check_win():
    lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
             (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
             (0, 4, 8), (2, 4, 6)]             # diagonals
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != EMPTY:
            return True
    return False

def check_tie():
    return EMPTY not in board

def switch_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'

while True:
    print_board(board)
    position = player_input()
    board[position] = current_player
    if check_win():
        print_board(board)
        print(f"Player {current_player} wins!")
        break
    if check_tie():
        print_board(board)
        print("It's a tie!")
        break
    switch_player()