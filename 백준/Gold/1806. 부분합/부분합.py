import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
s = int(data[1])
nums = list(map(int, data[2:]))

start = 0
end = 0
sum = 0
min_length = float('inf')

while True:
    if sum >= s:
        min_length = min(min_length, end - start)
        sum -= nums[start]
        start += 1
    elif end == n:
        break
    else:
        sum += nums[end]
        end += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)
