from collections import deque

def solution(arr):
    answer = []
    # q_arr = deque(arr)
    for n in arr:
        if (len(answer) == 0) or (n != answer[-1]):
            answer.append(n)
    return answer