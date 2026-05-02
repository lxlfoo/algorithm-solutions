def solution(sequence, k):
    n = len(sequence)
    left = 0
    sum = 0
    answer = [0, n]

    for right in range(n):
        sum += sequence[right]

        while sum > k:
            sum -= sequence[left]
            left += 1

        if sum == k:
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]

    return answer
