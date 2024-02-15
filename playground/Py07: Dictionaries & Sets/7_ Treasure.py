def treasure(clues):
    go_to = (0, 0)
    next = clues.keys()
    while True:
        if go_to in next:
            have_been_to = go_to
            go_to = clues[go_to]
            clues.pop(have_been_to)

        else:
            return go_to