# 최소직사각형
# 완전탐색
# 정답률: 70% 
# 2023.02.23
# 13:00 ~ 13:30 (30 min)
# 후기: 처음에 조건문으로 해결하려해서 다소 시간이 걸렸지만, 문제를 다시 읽고 min,max로 접근해서 문제를 해결함


def solution(sizes):
    answer = 0
    max_w = 0
    max_h = 0
    max_total = 0
    check_inv = 0
    
    for i in sizes:
        max_total = max(max_total,max(i[0],i[1]))
        if max_total == i[0]:
            check_inv = 0
        if max_total == i[1]:
            check_inv = 1
            
    for i in sizes:
        if check_inv == 0:
            if max_w < i[0]:
                max_w = i[0]
            if max_h < i[1]:
                max_h = max(max_h,min(i[0],i[1]))
                
        if check_inv == 1:
            if max_h < i[1]:
                max_h = i[1]
            if max_w < i[0]:
                max_w = max(max_w,min(i[0],i[1]))
    
    answer = max_w * max_h
    return answer

