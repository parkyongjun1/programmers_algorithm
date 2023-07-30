# 덧칠하기
# practice problem
# 정답률: 59% 
# 2023.07.21
# 15:00 ~ 15:05 (5 min)
# 후기: len check을 통해 cnt를 써서 쉽게 문제를 해결.

def solution(n, m, section):
    answer = 0
    len_check = 0
    cnt = 0
    
    for idx, i in enumerate(section):
        if idx == 0:
            len_check = i+m-0.5
            cnt += 1
            continue
        else:
            if i > len_check:
                len_check = i+m-0.5
                cnt += 1
    return cnt