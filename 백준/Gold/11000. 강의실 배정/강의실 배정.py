import sys
import heapq

input = sys.stdin.read().split()

n = int(input[0])
lectures = []

idx = 1
for _ in range(n):
    s = int(input[idx])
    t = int(input[idx+1])
    lectures.append((s, t))
    idx += 2

lectures.sort()

room = []
heapq.heappush(room, lectures[0][1])

for i in range(1, n):
    if room[0] <= lectures[i][0]:
        heapq.heappop(room)

    heapq.heappush(room, lectures[i][1])

print(len(room))
