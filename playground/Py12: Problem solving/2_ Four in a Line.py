DIC = {1: "red", 2: "yellow"}
def four_in_line(board):
    #check in lines
    for row in board:
        for x in range(2):
            if row[x] in DIC and row[x] == row[x+1] == row[x+2] == row[x+3]:
                bigging = (board.index(row), x)
                end = (board.index(row), x+3)
                return {bigging, end}
    
    #check for collums
    for collums in range(len(board[0])):
        for row in range(len(board)-3):
            if board[row][collums] in DIC and board[row][collums] == board[row+1][collums] == board[row+2][collums] == board[row+3][collums]:
                return {(row, collums), (row+3, collums)}
    
    for collums in range(len(board[0])):
        for row in range(len(board)):
            try:
                if board[row][collums] in DIC and board[row][collums] == board[row-1][collums+1] == board[row-2][collums+2] == board[row-3][collums+3]:
                    return {(row, collums), (row-3, collums+3)}
            except:
                pass
            try:
                if board[row][collums] in DIC and board[row][collums] == board[row+1][collums+1] == board[row+2][collums+2] == board[row+3][collums+3]:
                    return {(row, collums), (row+3, collums+3)}
            except:
                continue


            
print(four_in_line([
    [0, 2, 0, 0, 0], 
    [0, 2, 2, 0, 0], 
    [0, 2, 2, 2, 1], 
    [0, 1, 1, 1, 2], 
    [0, 1, 1, 2, 2]]))
