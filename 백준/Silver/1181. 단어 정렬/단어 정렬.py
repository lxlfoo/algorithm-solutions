import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
words = list(set(data[1:]))
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
