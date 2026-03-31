import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

dp_inc = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

dp_dec = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[j] < a[i]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)

rst = 0
for i in range(n):
    rst = max(rst, dp_inc[i] + dp_dec[i] - 1)

print(rst)
