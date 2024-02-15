def palindrome_index(s):
    if is_palindrome(s):
        return -1
    for i in range(len(s)):
        if is_palindrome(s[:i]+s[i+1:]):
            return i
        
    return -1

def is_palindrome(s):
    return s == s[::-1]
