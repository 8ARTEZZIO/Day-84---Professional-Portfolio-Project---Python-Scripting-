def display_board(board):
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")

def check_win(board, player):
    # horizontal
    if board[:3] == [player]*3 or board[3:6] == [player]*3 or board[6:] == [player]*3:
        return True
    # vertical
    for i in range(3):
        if [board[i+0], board[i+3], board[i+6]] == [player]*3:
            return True
    # diagonal
    if [board[0], board[4], board[8]] == [player]*3:
        return True

    elif [board[6], board[4], board[2]] == [player]*3:
        return True

    return False


if __name__ == '__main__':
    game_on = True
    board = [i for i in range(9)] # initialize a board
    player = "o"
    o, x = 0, 0

    while game_on:      # display a board

        player_move = []
        while player_move not in [i for i in range(9)]:
            display_board(board)
            try:
                player_move = int(input("Choose a spot on a board [0-8]: "))
            except ValueError:
                print('Provided spot must be a [0-8] num:')
            else:
                print('Provided spot must be a [0-8] num:')

        board[player_move] = player

        if check_win(board, player):
            game_on = False
            display_board(board)
            print(f"Player {player} won!")
            if player == "o":
                o += 1
            elif player == "x":
                x += 1
            print(f"Current score:\n\tplayer o: {o}\n\tplayer x: {x}")


        player = "x" if player == "o" else "o"
