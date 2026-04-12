import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())

fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    dict_grid = {}

    for i in range(len(fireballs)):
        curr_fb = fireballs[i]
        f_r = curr_fb[0]
        f_c = curr_fb[1]
        f_m = curr_fb[2]
        f_s = curr_fb[3]
        f_d = curr_fb[4]

        nr = (f_r + dr[f_d] * f_s) % N
        nc = (f_c + dc[f_d] * f_s) % N

        pos = (nr, nc)
        if pos not in dict_grid:
            dict_grid[pos] = []
        dict_grid[pos].append([f_m, f_s, f_d])

    new_fireballs = []

    for key in dict_grid.keys():
        r, c = key
        target = dict_grid[key]

        if len(target) == 1:
            b = target[0]
            new_fireballs.append([r, c, b[0], b[1], b[2]])
        else:
            total_m = 0
            total_s = 0
            cnt = len(target)

            even_cnt = 0
            odd_cnt = 0

            for b in target:
                total_m += b[0]
                total_s += b[1]
                if b[2] % 2 == 0:
                    even_cnt += 1
                else:
                    odd_cnt += 1

            new_m = total_m // 5
            if new_m > 0:
                new_s = total_s // cnt

                if even_cnt == cnt or odd_cnt == cnt:
                    directions = [0, 2, 4, 6]
                else:
                    directions = [1, 3, 5, 7]

                for next_d in directions:
                    new_fireballs.append([r, c, new_m, new_s, next_d])

    fireballs = new_fireballs

sum = 0
for f in fireballs:
    sum += f[2]

print(sum)
