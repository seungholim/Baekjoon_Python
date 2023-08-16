def solution(sides):
    a = sorted(sides)
    if a[0] + a[1] > a[2]:
        answer = 1
    else:
        answer = 2
    return answer