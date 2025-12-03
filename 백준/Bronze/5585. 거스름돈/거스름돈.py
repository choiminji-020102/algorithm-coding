price = int(input())

change = 1000 - price

coin = [500, 100, 50, 10, 5, 1]
result = 0

for c in coin:
    cnt = change // c
    result += cnt
    change = change % c

print(result)