def solution(order):
    a = str(order)
    cnt = 0
    for i in a:
        if i == '3' or i == '6' or i == '9':
            cnt += 1
    return cnt