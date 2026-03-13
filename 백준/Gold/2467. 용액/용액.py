import sys

input = sys.stdin.readline
n = int(input())
solutions = list(map(int, input().split()))

left = 0
right = n - 1

zero_sum = float('inf')
feats = [0, 0]

while left < right:
    sum = solutions[left] + solutions[right]

    if abs(sum) < zero_sum:
        zero_sum = abs(sum)
        feats = [solutions[left], solutions[right]]

    if sum == 0:
        break

    if sum < 0:
        left += 1
    else:
        right -= 1

print(feats[0], feats[1])
