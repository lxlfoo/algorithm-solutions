def solution(myString, pat):
    str = "".join(['B' if char == 'A' else 'A' for char in myString])

    return 1 if pat in str else 0
