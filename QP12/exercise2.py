def tic_tac_toe(board, player):
    board = board.split("\n")
    pos = {1:"A", 2:"B", 3:"C"}
    for n_lin in range(len(board)):
        for char in range(3):
            if board[n_lin][char] == " ":
                t = board[n_lin][:char] + player + board[n_lin][char+1:]
                board1 = board[:n_lin] + [t] + board[n_lin+1:]
                if check(board1, player):
                    return pos[n_lin+1]+str(char+1)

def check(board, player):
    #lines
    for x in board:
        if x.count(x[0]) == 3:
            return True
    #rows
    for x in range(len(board)):
        row = board[0][x] + board[1][x] + board[2][x]
        if row == 3*player:
            return True
    if board[0][0] + board[1][1] + board[2][2] == 3*player:
        return True
    elif board[2][0] + board[1][1] + board[0][2] == 3*player:
        return True
    return False
