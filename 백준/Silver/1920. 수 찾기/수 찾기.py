import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

A.sort()
for d in data:
    result = 0
    left_i, right_i = 0, N-1
    mid_i = (left_i + right_i) // 2
    
    while left_i<=right_i:
        if d == A[mid_i]:
            result = 1
            break
        elif d < A[mid_i]: 
            right_i = mid_i - 1
            mid_i = (left_i + right_i) // 2

        elif A[mid_i] < d:
            left_i = mid_i + 1
            mid_i = (left_i + right_i) // 2

    print(result)
    

        