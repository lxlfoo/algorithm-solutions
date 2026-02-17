import sys

input = sys.stdin.readline
n, m = map(int, input().split())

s = set()
for _ in range(n):
    s.add(input().strip())

count = 0
for _ in range(m):
    if input().strip() in s:
        count += 1

print(count)
