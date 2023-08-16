def solution(n):
    a = list(str(n))
    answer = []
    for i in a:
        answer.append(int(i))
    return sum(answer)