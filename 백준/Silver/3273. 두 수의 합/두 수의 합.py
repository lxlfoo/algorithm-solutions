import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

cnt = 0
left = 0
right = n - 1

while left < right:
    sum = nums[left] + nums[right]

    if sum == x:
        cnt += 1
        left += 1
        right -= 1
    elif sum < x:
        left += 1
    else:
        right -= 1

print(cnt)
