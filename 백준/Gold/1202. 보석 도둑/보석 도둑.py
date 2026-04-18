import sys
import heapq

input = sys.stdin.read().split()

N = int(input[0])
K = int(input[1])

jewels = []
idx = 2
for _ in range(N):
    jewels.append((int(input[idx]), int(input[idx+1])))
    idx += 2

bags = []
for _ in range(K):
    bags.append(int(input[idx]))
    idx += 1

jewels.sort()
bags.sort()

rst = 0
cand = []
pointer = 0

for bag in bags:
    while pointer < N and jewels[pointer][0] <= bag:
        heapq.heappush(cand, -jewels[pointer][1])
        pointer += 1

    if cand:
        rst -= heapq.heappop(cand)

print(rst)
