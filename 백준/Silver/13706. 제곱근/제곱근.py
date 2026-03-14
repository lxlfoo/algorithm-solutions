import sys

input = sys.stdin.readline
n = int(input())

low = 0
high = n

while low <= high:
    mid = (low + high) // 2
    sqr = mid * mid

    if sqr == n:
        print(mid)
        break
    elif sqr < n:
        low = mid + 1
    else:
        high = mid - 1
