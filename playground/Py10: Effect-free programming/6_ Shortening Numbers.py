def shorten(suffixes, base):
    def number(n):
        if (type(n) != str) or (int(n) <= 0):
            return str(n)
        t = len(suffixes)-1
        while True:
            if int(n) > int(int(base)**t):
                return f"{n[:len(n) - len(str(int(base)**t)) +1]} {suffixes[t]}"
            t = t-1
    return number
print(shorten(["B", "KiB", "MiB", "GiB", "TiB"], 1024)("0"))