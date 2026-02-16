def divide_conquer(a, b, c):
    if b == 0:
        return 1

    half = divide_conquer(a, b // 2, c)

    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

A, B, C = map(int, input().split())
print(divide_conquer(A, B, C))
