def longest(filename):
    with open(filename) as f:
        words = f.read().split()
        return max(words, key=len)

file = 'shakespeare.txt'
print(longest(file))