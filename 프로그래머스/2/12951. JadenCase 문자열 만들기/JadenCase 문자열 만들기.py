def solution(s):
    words = s.split(' ')

    result = []
    for word in words:
        if word:
            result.append(word.capitalize())
        else:
            result.append('')

    answer = ' '.join(result)
    return answer
