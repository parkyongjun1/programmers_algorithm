# 모의고사
# 완전탐색
# 정답률: 62% 
# 2023.10.11
# 13:50 ~ 14:45 (55 min)
# 후기: 반복되는 리스트의 나머지를 이용해 인덱스를 구하고, max값을 리턴해 문제를 해결함.

def solution(answers):
    answer = []
    p1_num = [1,2,3,4,5]
    p2_num = [2,1,2,3,2,4,2,5]
    p3_num = [3,3,1,1,2,2,4,4,5,5]
    p1_idx,p2_idx,p3_idx = 0,0,0
    score = [0,0,0]
    
    for idx, i in enumerate(answers, start=1):
        p1_idx = idx%len(p1_num)-1
        p2_idx = idx%len(p2_num)-1
        p3_idx = idx%len(p3_num)-1
        
        if i == p1_num[p1_idx]:
            score[0] += 1
        if i == p2_num[p2_idx]:
            score[1] += 1
        if i == p3_num[p3_idx]:
            score[2] += 1
            
    for idx, i in enumerate(score,start = 1):
        if max(score) == i:
            answer.append(idx)
            
    return answer