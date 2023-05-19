board = [' '] * 9

def print_board():
    """
    Prints the current state of the board.
    """
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')

def check_win():
    """
    Checks if either player has won the game.
    """
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

def check_tie():
    """
    Checks if the game is tied.
    """
    return ' ' not in board

def make_move(player):
    """
    Gets the player's move and updates the board.
    """
    while True:
        move = int(input(f"{player}'s turn. Enter a position from 1-9: ")) - 1
        if board[move] == ' ':
            board[move] = player
            break
        else:
            print('Invalid move. Try again.')

def play_game():
    """
    Runs the Tic Tac Toe game.
    """
    print('Welcome to Tic Tac Toe!')
    print_board()
    player = 'X'
    while True:
        make_move(player)
        print_board()
        if check_win():
            print(f'{player} wins!')
            break
        elif check_tie():
            print('Game tied.')
            break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
