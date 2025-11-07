import random

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def check_draw():
    return ' ' not in board

def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That position is already filled!")
        except (ValueError, IndexError):
            print("Invalid input! Enter number between 1-9.")

def computer_move():
    print("Computer is thinking...")
    # Try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner('O'):
                return
            board[i] = ' '
    # Try to block player
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner('X'):
                board[i] = 'O'
                return
            board[i] = ' '
    # Otherwise choose random
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = 'O'
            break

def main():
    print("🎮 Welcome to Advanced Tic-Tac-Toe Game!")
    print("You are X, Computer is O.")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner('X'):
            print("2You Win!")
            break
        if check_draw():
            print("It's a Draw!")
            break

        computer_move()
        print_board()
        if check_winner('O'):
            print("Computer Wins!")
            break
        if check_draw():
            print("It's a Draw!")
            break

main()
