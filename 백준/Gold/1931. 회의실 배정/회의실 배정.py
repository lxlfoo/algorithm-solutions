import sys

input = sys.stdin.read().split()

n = int(input[0])
meetings = []

for i in range(n):
    start = int(input[2*i + 1])
    end = int(input[2*i + 2])
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
limit = 0

for start, end in meetings:
    if start >= limit:
        count += 1
        limit = end

print(count)
