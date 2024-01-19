def preorder(tree, result = []):
    left = None
    right = None
    result = [tree[0]]
    if type(tree[1]) == tuple:
        left = preorder(tree[1])
        list(map(lambda x: result.append(x), left))
    elif tree[1] != None:
        left = tree[1]
        result.append(left)
    
    if type(tree[2]) == tuple:
        right = preorder(tree[2])
        list(map(lambda x: result.append(x), right))
    elif tree[2] != None:
        right = tree[2]
        result.append(right)

    return result