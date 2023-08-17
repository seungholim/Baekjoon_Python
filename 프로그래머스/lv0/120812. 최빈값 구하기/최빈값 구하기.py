import operator
from collections import Counter

def solution(array):
    array_dict = Counter(array)
    array_dict = dict(array_dict)
    sorted_array_dict = sorted(array_dict.items(), key = lambda x:x[1])
    if len(sorted_array_dict) == 1:
        answer = sorted_array_dict[0][0]
    elif sorted_array_dict[-1][1] == sorted_array_dict[-2][1]:
        answer = -1
    elif sorted_array_dict[-1][1] != sorted_array_dict[-2][1]:
        answer = sorted_array_dict[-1][0]
    return answer