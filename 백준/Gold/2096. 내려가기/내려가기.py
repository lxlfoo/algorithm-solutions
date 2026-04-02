import sys

input = sys.stdin.read().split()

n = int(input[0])
row = [int(input[1]), int(input[2]), int(input[3])]

max_dp = row[:]
min_dp = row[:]

idx = 4
for _ in range(n - 1):
    a, b, c = int(input[idx]), int(input[idx+1]), int(input[idx+2])
    idx += 3

    max_next = [
        a + max(max_dp[0], max_dp[1]),
        b + max(max_dp[0], max_dp[1], max_dp[2]),
        c + max(max_dp[1], max_dp[2])
    ]

    min_next = [
        a + min(min_dp[0], min_dp[1]),
        b + min(min_dp[0], min_dp[1], min_dp[2]),
        c + min(min_dp[1], min_dp[2])
    ]

    max_dp = max_next
    min_dp = min_next

print(max(max_dp), min(min_dp))
