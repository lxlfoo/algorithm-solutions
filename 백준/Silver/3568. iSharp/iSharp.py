import sys

input = sys.stdin.readline
statement = input().split()

first = statement[0]
last = statement[1:]

for var in last:
    var = var.replace(',', '').replace(';', '')
    name, symbol = '', ''

    for c in var:
        if c.isalpha():
            name += c
        else:
            symbol += c

    rsymbol = ''
    i = len(symbol) - 1

    while i >= 0:
        if symbol[i] == ']':
            rsymbol += '[]'
            i -= 2
        elif symbol[i] == '[':
            i -= 1
        else:
            rsymbol += symbol[i]
            i -= 1

    print(f'{first}{rsymbol} {name};')
