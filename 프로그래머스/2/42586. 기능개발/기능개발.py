from math import ceil

def solution(progresses, speeds):
    answer = []
    remainDay = []
    for i, p in enumerate(progresses):
        # print((100 - p) // speeds[i]) # 몫
        # print((100 - p) % speeds[i]) # 나머지
        remainDay.append(ceil((100 - p) / speeds[i]))
    max = remainDay[0]
    hap = 0
    for i, r in enumerate(remainDay):
        if max < r:
            answer.append(hap)
            hap = 1
            max = r
        elif max >= r:
            hap += 1 
        if (i+1) == len(remainDay):
            answer.append(hap)
    return answer