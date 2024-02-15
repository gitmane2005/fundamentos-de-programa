lower = int(input())
upper = int(input())

print(f"Prime numbers between {lower} and {upper} are: ", end="")
for i in range(lower,upper+1):
    if i > 1 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 or (i == 2 or i == 3 or i == 5):
        print(i, end=" ")
    else:
        continue
print("")