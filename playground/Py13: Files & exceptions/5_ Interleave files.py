def interleave(f1, f2):
    res = ""
    with open(f1) as file1, open(f2) as file2:
        for line1, line2 in zip(file1,file2):
            res += line1 + line2
    return res
print(interleave("monty.txt", 'shakespeare.txt'))