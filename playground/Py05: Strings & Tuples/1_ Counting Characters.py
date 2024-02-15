def count_chars(a_string):
    alphabetic = 0
    digits = 0
    special_symbols = 0
    for char in a_string:
        if char.isalpha():
            alphabetic += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1

    return(alphabetic,digits,special_symbols)