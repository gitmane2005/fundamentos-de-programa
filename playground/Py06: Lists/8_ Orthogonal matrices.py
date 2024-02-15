def transpose_matrix(m):
    result = [[],[]]
    for i in m:
        for b in range(len(i)):
            result[b].append(i[b])
    
    return result

def is_orthogonal(mx):
    result = [[],[]]
    
    mx_transpose = transpose_matrix(mx)
    for a in range(len(mx)):
        for b in range(len(mx)):
            result[a].append(mx[a][b]*mx_transpose[b][a])

    ident = [[1,0],[0,1]]

    return ident == result