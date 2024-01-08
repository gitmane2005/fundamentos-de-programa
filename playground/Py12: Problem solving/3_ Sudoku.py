def solve_sudoku(board):
    for line in board:
        if sum(line) != 45 and line.count(0) == 1:
            board[board.index(line)][line.index(0)] = (45- sum(line))
            continue
        for collum in range(len(board[0])):
            if board[board.index(line)][collum] == 0:
                board[board.index(line)][collum] = 45 - sum([board[x][collum] for x in range(len(board[0]))])
    return board
print(solve_sudoku([[9, 3, 7, 1, 4, 2, 5, 8, 6], [5, 6, 2, 7, 3, 8, 1, 4, 0], [4, 8, 1, 9, 5, 6, 7, 2, 3], [1, 4, 6, 0, 9, 3, 8, 5, 0], [3, 2, 5, 6, 8, 7, 9, 1, 4], [8, 7, 9, 4, 0, 5, 3, 6, 2], [7, 9, 4, 8, 2, 1, 6, 3, 5], [6, 5, 8, 3, 7, 4, 2, 9, 1], [2, 1, 3, 5, 6, 9, 4, 7, 8]]))
