import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

shark_x, shark_y = 0, 0
shark_size = 2
count = 0
total_time = 0

for r in range(n):
    for c in range(n):
        if board[r][c] == 9:
            shark_x, shark_y = r, c
            board[r][c] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    q = deque([(shark_x, shark_y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[shark_x][shark_y] = True

    fish = []
    min_dist = float('inf')

    while q:
        x, y, dist = q.popleft()

        if dist > min_dist:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    if 0 < board[nx][ny] < shark_size:
                        min_dist = dist + 1
                        fish.append((dist + 1, nx, ny))
                    else:
                        q.append((nx, ny, dist + 1))

    if not fish:
        break

    fish.sort()
    dist, next_x, next_y = fish[0]

    total_time += dist
    shark_x, shark_y = next_x, next_y
    board[next_x][next_y] = 0
    count += 1

    if count == shark_size:
        shark_size += 1
        count = 0

print(total_time)
