import sys

input = sys.stdin.readline
n = int(input())

for i in range(1, n + 1):
    url = input().strip()

    delim = url.find('://')
    protocol = url[:delim]
    part = url[delim + 3:]

    path_start = part.find('/')

    if path_start != -1:
        path = part[path_start + 1:]
        part = part[:path_start]
    else:
        path = '<default>'

    port_start = part.find(':')

    if port_start != -1:
        host = part[:port_start]
        port = part[port_start + 1:]
    else:
        host = part
        port = '<default>'

    print(f'URL #{i}')
    print(f'Protocol = {protocol}')
    print(f'Host     = {host}')
    print(f'Port     = {port}')
    print(f'Path     = {path}')
    print()
