def complete_pairs(s1, s2):
    test = sorted("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
    result = set()
    for string_a in s1:
        for string_b in s2:
            possible_string = string_a+string_b
            possible_string_1 = sorted(list(set(possible_string)))
            if test == possible_string_1:
                result.add(possible_string)

    return result
