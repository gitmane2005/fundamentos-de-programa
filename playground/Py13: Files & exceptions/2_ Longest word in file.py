def longest(filename):
    with open(filename) as f:
        words = f.read().split()
        print(f.head())
        return max(words, key=len)

file = 'shakespeare.txt'
print(longest(file))