def search_map(map, map_rectangle, search_rectangle):
    if type(map) != tuple and overlap(map_rectangle, search_rectangle):
        return {map}  # Return a set with the matching element
    else:
        sub_width = map_rectangle[2] // 2
        sub_height = map_rectangle[3] // 2
        result = set()

        q1 = map[0]
        q1_map_rectangle = (map_rectangle[0], map_rectangle[1], sub_width, sub_height)
        if type(q1) == tuple:
            t = search_map(q1, q1_map_rectangle, search_rectangle)
            if t is not None:
                result.update(t)
        elif overlap(q1_map_rectangle, search_rectangle) and q1 is not None:
            result.add(q1)

        q2 = map[1]
        q2_map_rectangle = (map_rectangle[0] + sub_width, map_rectangle[1], sub_width, sub_height)
        if type(q2) == tuple:
            t = search_map(q2, q2_map_rectangle, search_rectangle)
            if t is not None:
                result.update(t)
        elif overlap(q2_map_rectangle, search_rectangle) and q2 is not None:
            result.add(q2)

        q3 = map[2]
        q3_map_rectangle = (map_rectangle[0] + sub_width, map_rectangle[1] + sub_height, sub_width, sub_height)
        if type(q3) == tuple:
            t = search_map(q3, q3_map_rectangle, search_rectangle)
            if t is not None:
                result.update(t)
        elif overlap(q3_map_rectangle, search_rectangle) and q3 is not None:
            result.add(q3)

        q4 = map[3]
        q4_map_rectangle = (map_rectangle[0], map_rectangle[1] + sub_height, sub_width, sub_height)
        if type(q4) == tuple:
            t = search_map(q4, q4_map_rectangle, search_rectangle)
            if t is not None:
                result.update(t)
        elif overlap(q4_map_rectangle, search_rectangle) and q4 is not None:
            result.add(q4)

    return result

def overlap(rect1, rect2):
    rect1_bl = (rect1[0], rect1[1])
    rect1_tr = (rect1[0] + rect1[2], rect1[1] + rect1[3])

    rect2_bl = (rect2[0], rect2[1])
    rect2_tr = (rect2[0] + rect2[2], rect2[1] + rect2[3])

    if (rect2_bl[0] > rect1_tr[0]) or (rect2_tr[0] < rect1_bl[0]):
        return False
    elif (rect1_tr[1] < rect2_bl[1]) or (rect1_bl[1] > rect2_tr[1]):
        return False
    else:
        return True



print(search_map(((None, (None, (None, 'b', (None, None, ((None, (('V', None, (('J', 'C', None, None), None, None, 'R'), None), None, None, 'W'), 'Y', None), None, None, None), 'Z'), None), None, None), None, None), ('f', None, None, ('X', None, ((None, 'L', ('K', None, 'D', None), None), None, None, 'T'), None)), (None, ('g', ('c', (None, None, None, ((None, (((None, None, ((None, (None, None, 'O', ('I', (None, None, 'H', (None, 'G', None, (('F', None, 'B', None), None, None, None))), None, None)), None, None), None, None, None), None), None, None, None), None, 'P', None), None, None), 'S', None, None)), None, None), None, None), None, None), (None, 'e', (None, ('a', (None, None, None, ('U', None, ('Q', (None, None, ('N', None, ('M', None, None, (None, 'E', None, 'A')), None), None), None, None), None)), None, None), None, 'd'), None)), (0, 0, 744, 1292), (504, 163, 238, 701)))