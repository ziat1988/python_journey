def generate_board():
    width = 3
    return [[' ' for i in range(width)] for i in range(width)]


def display_board():
    print(board)
    for arr in board:
        print('-' * 7)
        for cell in arr:
            print(f'|{cell}', end='')
        print('|')
    print('-' * 7)


def randomCellFill():
    board[0][0] = "O"
    board[0][1] = "O"
    board[0][2] = "X"

    board[1][0] = "X"
    board[1][1] = "X"
    # board[1][2] = "X"

    board[2][0] = "X"
    # board[2][1] = "O"
    board[2][2] = "O"


def validate_coordinate(move):
    try:
        x, y = int(move[0]), int(move[1])
        # get value board
        if board[x][y] != " ":
            raise ValueError('cell is occupied')

        # board[x][y] = player
        return True

    except ValueError as e:
        print("not valid interger allowed")
    except IndexError as e:
        print("not valid coord")

    return False


def check_draw():
    for i in board:
        if " " in i:
            return False
    return True


def check_win_position():
    # scan row
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            print('row win')
            return True

    # scan col
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            print('col win')
            return True

    # scan diagonal left
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print('diagonal left win')
        return True
    # scan diagonal right
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print('diagonal right win')
        return True

    return False


board = []


def main():
    while True:
        global board
        board = generate_board()
        display_board()
        winner = None
        player = "X"

        while winner is None:
            user_input = input(f'{player} plays:')
            if not (validate_coordinate(user_input)):
                continue
            print(user_input)
            board[int(user_input[0])][int(user_input[1])] = player
            display_board()

            if check_win_position():
                winner = player
                print(f'Congrat. Player {winner} is win!')

            if check_draw():
                print(f'Draw game')
                winner = "Draw"

            player = "X" if player == "O" else "O"

        continueGame = input("Do you want to exit? (y): ")

        if continueGame == "y":
            break


main()
