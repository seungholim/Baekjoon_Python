def solution(numbers):
    numbers.sort()
    if numbers[0]*numbers[1]>numbers[-1]*numbers[-2]:
        answer = numbers[0]*numbers[1]
    elif numbers[0]*numbers[1]<=numbers[-1]*numbers[-2]:
        answer = numbers[-1]*numbers[-2]
    return answer