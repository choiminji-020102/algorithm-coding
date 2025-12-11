import sys
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
# print(N, M)
# print(cards)

C = []
visited = [False] * (N)   # False = 방문X
result = 0

def backtracking():
    global result

    if len(C) == 3:
        sumC = sum(C)
        if (sumC > result) and (sumC <= M):
            result = sumC
        return 

    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            C.append(cards[i])

            backtracking()

            C.pop()
            visited[i] = False


backtracking()
print(result)