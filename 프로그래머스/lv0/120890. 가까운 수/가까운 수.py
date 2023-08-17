def solution(array, n):
    b = []
    array.sort()
    for i in array:
        b.append(abs(n-i))
    return array[(b.index(min(b)))]