import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

cleaner = []
for i in range(R):
    if grid[i][0] == -1:
        cleaner.append(i)

def dust():
    temp_grid = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0:
                amount = grid[r][c] // 5
                count = 0
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != -1:
                        temp_grid[nr][nc] += amount
                        count += 1
                grid[r][c] -= amount * count

    for r in range(R):
        for c in range(C):
            grid[r][c] += temp_grid[r][c]

def clean_up():
    up = cleaner[0]

    for i in range(up - 1, 0, -1):
        grid[i][0] = grid[i-1][0]

    for i in range(C - 1):
        grid[0][i] = grid[0][i+1]

    for i in range(up):
        grid[i][C-1] = grid[i+1][C-1]

    for i in range(C - 1, 1, -1):
        grid[up][i] = grid[up][i-1]

    grid[up][1] = 0

def clean_down():
    down = cleaner[1]

    for i in range(down + 1, R - 1):
        grid[i][0] = grid[i+1][0]

    for i in range(C - 1):
        grid[R-1][i] = grid[R-1][i+1]

    for i in range(R - 1, down, -1):
        grid[i][C-1] = grid[i-1][C-1]

    for i in range(C - 1, 1, -1):
        grid[down][i] = grid[down][i-1]

    grid[down][1] = 0

for _ in range(T):
    dust()
    clean_up()
    clean_down()

print(sum(sum(row) for row in grid) + 2)
