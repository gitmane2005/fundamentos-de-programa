def repeated_letter(s):
    for a in range(len(s)):
        for b in range(a+1,len(s)):
            if s[a] == s[b]:
                return s[a]