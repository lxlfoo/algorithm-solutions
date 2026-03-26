import sys
import heapq

input = sys.stdin.readline
n = int(input())

minheap = []
for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(minheap, x)
    else:
        if minheap:
            print(heapq.heappop(minheap))
        else:
            print(0)
