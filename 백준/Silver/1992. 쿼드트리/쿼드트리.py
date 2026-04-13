import sys

input = sys.stdin.readline
n = int(input())

board = [list(input().strip()) for _ in range(n)]

def compress(r, c, size):
    color = board[r][c]

    for i in range(r, r + size):
        for j in range(c, c + size):
            if board[i][j] != color:
                print('(', end='')
                half = size // 2
                compress(r, c, half)
                compress(r, c + half, half)
                compress(r + half, c, half)
                compress(r + half, c + half, half)
                print(')', end='')
                return

    print(color, end='')

compress(0, 0, n)
