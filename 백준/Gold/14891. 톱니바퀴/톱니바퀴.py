import sys
from collections import deque

input = sys.stdin.readline

gears = [deque(map(int, input().strip())) for _ in range(4)]

def rotate_gears(idx, direction):
    directions = [0] * 4
    directions[idx] = direction

    for i in range(idx, 0, -1):
        if gears[i-1][2] != gears[i][6]:
            directions[i-1] = -directions[i]
        else:
            break

    for i in range(idx, 3):
        if gears[i][2] != gears[i+1][6]:
            directions[i+1] = -directions[i]
        else:
            break

    for i in range(4):
        if directions[i] != 0:
            gears[i].rotate(directions[i])

k = int(input())

for _ in range(k):
    idx, d = map(int, input().split())
    rotate_gears(idx - 1, d)

rst = 0
for i in range(4):
    if gears[i][0] == 1:
        rst += (2 ** i)

print(rst)
