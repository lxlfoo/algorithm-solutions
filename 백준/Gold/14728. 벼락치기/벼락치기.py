import sys

input = sys.stdin.readline
n, t = map(int, input().split())

dp = [0] * (t + 1)

for _ in range(n):
	time, score = map(int, input().split())

	for j in range(t, time - 1, -1):
		if dp[j] < dp[j - time] + score:
			dp[j] = dp[j - time] + score

print(dp[t])
