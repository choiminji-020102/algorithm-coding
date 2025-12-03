## h의 최댓값!
# h = 0: 0편 이상 인용된 논문 -> 0,1,3,5,6 -> 5편 = 0편 이상 -> 조건 충족 O
# h = 1: 1편 이상 인용된 논문 -> 1,3,5,6 -> 4편 = 1편 이상 -> 조건 충족 O
# h = 2: 2편 이상 인용된 논문 -> 3,5,6 -> 3편 = 2편 이상 -> 조건 충족 O
# h = 3: 3편 이상 인용된 논문 -> 3,5,6 -> 3편 = 3편 이상 -> 조건 충족 O => 최댓값
# h = 4: 4편 이상 인용된 논문 -> 5,6 -> 2편 = 4편 이상 -> 조건 충족 X
# h = 5: 5편 이상 인용된 논문 -> 5,6 -> 2편 = 5편 이상 -> 조건 충족 X
# h = 6: 6편 이상 인용된 논문 -> 6 -> 2편 = 6편 이상 -> 조건 충족 X

def solution(citations):
    # 인용 횟수 정렬
    citations.sort() # [0,1,3,5,6]
    H_Index = 0
    for i in range(len(citations)):
        # cite_num: 현재 논문의 인용 횟수 (h의 후보)
        cite_num = citations[i]
        
        # paper_num: h번 이상 인용된 논문의 개수 (현재 위치부터 끝까지의 개수)
        paper_num = len(citations) - i
        
        if cite_num >= paper_num:
            return paper_num
        
    return 0