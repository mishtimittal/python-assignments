
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],  
        [0,3,6],[1,4,7],[2,5,8],  
        [0,4,8],[2,4,6]           
    ]
    for c in win_conditions:
        if board[c[0]] == board[c[1]] == board[c[2]] == player:
            return True
    return False


def check_tie(board):
    return " " not in board


def get_player_input(player, board):
    while True:
        pos = input(f"Player {player}, enter position (1-9): ")

        if not pos.isdigit():
            print("Enter a number!")
            continue

        pos = int(pos)

        if pos < 1 or pos > 9:
            print("Choose number 1–9!")
            continue

        if board[pos-1] != " ":
            print("Position taken. Try again.")
            continue

        return pos-1


def play_game():
    while True:
        board = [" "] * 9
        player = "X"

        while True:
            print_board(board)
            move = get_player_input(player, board)
            board[move] = player

            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break

            if check_tie(board):
                print_board(board)
                print("It's a tie!")
                break

            player = "O" if player == "X" else "X"

        again = input("Play again? (y/n): ")
        if again.lower() != "y":
            print("Goodbye!")
            break
