from math import sqrt as sr
def fibonacci_sequence(n):
    a = (1+sr(5))**n
    b = (1-sr(5))**n
    c = (2**n)*sr(5)
    return int((a-b)/c)



def caesar(message):
    result = ""
    i = 0
    for char in message:
        if char.isalpha() == False:
            result += char
            
        else:    
            index = ord(char) - ord('A')
            shift = fibonacci_sequence(i)
            new_index = (index - shift) % 26
            new_unicode = new_index + ord('A')
            new_character = chr(new_unicode)
            result += new_character
        i += 1 
    
    return resultw