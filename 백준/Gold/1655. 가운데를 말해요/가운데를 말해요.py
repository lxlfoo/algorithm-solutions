import sys
import heapq

input = sys.stdin.readline

n = int(input())
leftheap = []
rightheap = []

for _ in range(n):
    number = int(input())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -number)
    else:
        heapq.heappush(rightheap, number)

    if rightheap and (-leftheap[0] > rightheap[0]):
        left_temp = -heapq.heappop(leftheap)
        right_temp = heapq.heappop(rightheap)

        heapq.heappush(leftheap, -right_temp)
        heapq.heappush(rightheap, left_temp)

    print(-leftheap[0])
