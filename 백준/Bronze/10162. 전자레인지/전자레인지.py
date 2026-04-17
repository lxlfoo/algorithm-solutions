import sys

input = sys.stdin.readline
t = int(input())

a = 300
b = 60
c = 10

if t % 10 != 0:
    print(-1)
else:
    cnt_a = t // a
    t %= a

    cnt_b = t // b
    t %= b

    cnt_c = t // c
    t %= c

    print(cnt_a, cnt_b, cnt_c)
