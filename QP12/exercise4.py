dic = {'E':(0,1), 
       'N':(-1,0), 
       'W':(0,-1),
       'S':(1,0)}
change_dic = {       
       ('\\','E'):'S',
       ('\\','W'):'N',
       ('\\','N'):'W',
       ('\\','S'):'E',
       
       ('/','E'):'N',
       ('/','W'):'S',
       ('/','N'):'E',
       ('/','S'):'W',}
def move_ball(board):
    pos, headed = find_bigining(board)
    path = [pos]
    while board[pos[0]][pos[1]] != "X":
        pos = (pos[0] + dic[headed][0], pos[1] + dic[headed][1])
        path = path + [pos]
        if board[pos[0]][pos[1]] == "\\" or board[pos[0]][pos[1]] == "/":
            headed = change_direction(board, pos, headed)
    return path

def change_direction(board, pos, corrent_headed):
    a = (board[pos[0]][pos[1]], corrent_headed)
    return change_dic[(board[pos[0]][pos[1]], corrent_headed)]

def find_bigining(board) :
    possible_starts = {'E', 'N', 'W', 'S'}
    for lin in range(len(board)):
        for char in range(len(board[lin])):
            if board[lin][char] in possible_starts:
                return ((lin, char), board[lin][char])

#print(move_ball(['E \\', '/ /', '   ', '\\ X']))