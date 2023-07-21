# 요격 시스템
# practive problem
# 정답률: 33% 
# 2023.07.21
# 13:10 ~ 14:50 (90 min)
# 후기: 처음에 범위가 겹치는 list에 대해 새로운 리스트에 추가 후 for문을 돌리는 방식으로 접근해서 헤맸다. target을 x[1]을 기준으로 정렬 후 범위를 고려하여 문제를 해결했다.

def solution(targets):
    targets.sort(key = lambda x: x[1])
    shoot = -1
    cnt = 0
    for target in targets:
        if target[0] > shoot :
            cnt += 1
            shoot = target[1]-0.5
            
    return cnt