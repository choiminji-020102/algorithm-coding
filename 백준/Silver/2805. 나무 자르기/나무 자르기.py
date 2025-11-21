import sys
N, M = map(int, sys.stdin.readline().split())
trees_tall = list(map(int, sys.stdin.readline().split()))

# 모든 나무를 높이 H를 기준으로 자른 뒤, 
# 잘라진 나무 토막들의 합이
# 상근이가 필요한 나무의 길이 M이어야 함.
# 잘라진 나무 토막들의 합 >= M
# H의 최댓값 구하기 = 최소한으로 잘라라
# H는 0보다 같거나 크고, ('나무들의 키 중 최댓값' - 1) 보다는 작음 (H는 1이상이기 때문) => 이 안에서 이진 탐색으로 찾아야겠다
max_tall = max(trees_tall)
left, right = 0, max_tall
mid = (left + right) // 2   # = H
best_H = 0

while left <= right:
    mid = (left + right) // 2
    def sum_tomak(trees_tall, mid):
        tomak_sum = 0
        for t in trees_tall:
            if t - mid > 0:
                tomak_sum += t - mid
        return tomak_sum

    if sum_tomak(trees_tall, mid) < M:
        right = mid - 1
        
    else:
        best_H = mid
        left = mid + 1


print(best_H)