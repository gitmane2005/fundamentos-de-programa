def discard_middle(s):
    if len(s) <= 3:
        return ""
    
    return s[:2] + s[len(s)-2:]