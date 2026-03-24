import sys
import heapq

input = sys.stdin.read

data = input().split()
n = int(data[0])
ops = data[1:]

maxheap = []
rst = []

for i in range(n):
    x = int(ops[i])

    if x > 0:
        heapq.heappush(maxheap, -x)
    else:
        if not maxheap:
            rst.append('0')
        else:
            rst.append(str(-heapq.heappop(maxheap)))

print('\n'.join(rst))
