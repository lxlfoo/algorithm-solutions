import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub(r'[^a-z0-9\-_.]', '', answer)
    answer = re.sub(r'\.+', '.', answer)
    answer = re.sub(r'^\.|\.$', '', answer)

    if not answer:
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]
        answer = re.sub(r'\.$', '', answer)

    while len(answer) < 3:
        answer += answer[-1]

    return answer
