import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    num = int(input().strip())

    if num != 0:
        heapq.heappush(arr, (abs(num), num))
    else:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
