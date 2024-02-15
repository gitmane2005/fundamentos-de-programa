n = int(input())

while n != 0:
    for i in range(n, 0, -1):
        print(i, end=" ")
    n = n - 1
    print("")