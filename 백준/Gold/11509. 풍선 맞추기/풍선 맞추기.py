import sys

input = sys.stdin.readline
_ = int(input())
balloons = list(map(int, input().split()))

arrow_heights = [0] * 1000001
arrow_count = 0

for h in balloons:
    if arrow_heights[h] > 0:
        arrow_heights[h] -= 1
        arrow_heights[h-1] += 1
    else:
        arrow_count += 1
        arrow_heights[h-1] += 1

print(arrow_count)
