import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input().strip())
    arr = input().strip()

    if n == 0:
        dq = deque()
    else:
        dq = deque(arr[1:-1].split(','))

    is_reversed = False
    is_error = False

    for ch in p:
        if ch == 'R':
            is_reversed = not is_reversed
        elif ch == 'D':
            if not dq:
                is_error = True
                break

            if is_reversed:
                dq.pop()
            else:
                dq.popleft()

    if is_error:
        print('error')
    else:
        if is_reversed:
            dq.reverse()
        print('[' + ','.join(dq) + ']')
