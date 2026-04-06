import sys

input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
r, c, d = int(data[2]), int(data[3]), int(data[4])

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

area = []
idx = 5
for i in range(n):
    area.append(list(map(int, data[idx:idx+m])))
    idx += m

count = 0

while True:
    if area[r][c] == 0:
        area[r][c] = 2
        count += 1

    empty = False
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if area[nr][nc] == 0:
                empty = True
                break

    if not empty:
        back_d = (d + 2) % 4
        nr, nc = r + dr[back_d], c + dc[back_d]

        if 0 <= nr < n and 0 <= nc < m and area[nr][nc] != 1:
            r, c = nr, nc
        else:
            print(count)
            break
    else:
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < n and 0 <= nc < m and area[nr][nc] == 0:
            r, c = nr, nc
