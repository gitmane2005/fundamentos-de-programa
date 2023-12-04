def search_tree(key, tree):
    if (tree == None):
        return None
    elif tree[0] == key:
        return (tree[1], [tree[0]])
    elif search_tree(key, tree[2]) != None:
        t = search_tree(key, tree[2])
        x = [tree[0]] + t[1]
        return (t[0], x)
    elif search_tree(key, tree[3]) != None:
        t = search_tree(key, tree[3])
        x = [tree[0]] + t[1]
        return (t[0], x)
    return None
