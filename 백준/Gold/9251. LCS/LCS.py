import sys

input = sys.stdin.readline
lcs1 = input().strip()
lcs2 = input().strip()

r = len(lcs1)
c = len(lcs2)

matrix = [[0] * (c + 1) for _ in range(r + 1)]

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if lcs1[i-1] == lcs2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[r][c])
