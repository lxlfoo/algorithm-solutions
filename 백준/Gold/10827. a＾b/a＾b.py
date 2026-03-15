import sys

line = sys.stdin.readline().strip()
s, b = line.split()
b = int(b)

if '.' in s:
    p = len(s) - s.find('.') - 1
    a = int(s.replace('.', ''))
    point = p * b
else:
    a = int(s)
    point = 0

result = str(a ** b)

if point == 0:
    print(result)
else:
    if len(result) <= point:
        result = '0' * (point - len(result) + 1) + result

    idx = len(result) - point
    print(result[:idx] + '.' + result[idx:])
