import sys

input = sys.stdin.readline
n = int(input())

words = []
for _ in range(n):
    words.append(input().strip())

words_list = sorted(list(set(words)))

prefix_count = 0
words_count = len(words_list)

for i in range(words_count):
    is_prefix = False
    for j in range(i + 1, words_count):
        if words_list[j].startswith(words_list[i]):
            is_prefix = True
            break

    if not is_prefix:
        prefix_count += 1

print(prefix_count)
