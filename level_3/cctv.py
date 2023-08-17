# 2023.08.17
# 17:30 ~ 16:00 (30 min)
# 후기: 저번에 해결했던 level2 미사일 요격 시스템에서와 같이 정렬 후 기준선에 따라 카운트를 이용해 해결함.

def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    
    check_line = -300001
    cnt = 0
    for route in routes:
            if route[1] > check_line and route[0] > check_line:
                cnt += 1
                check_line = route[1]+0.5
    return cnt