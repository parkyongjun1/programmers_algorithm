# 크기가 작은 부분문자열
# practive problem
# 정답률: 64% 
# 2023.02.15
# 14:30 ~ 14:45 (15 min)
# 후기: 문제를 이해하고 어렵지 않게 해결 할 수 있었음. 


def solution(t, p):
    answer = 0
    check_num = 0
    check_cnt = 0
    for  i in range(len(t)):
        check_len = len(p)
        if i+check_len > len(t):
            pass
        else:
            check_num = int(t[i:i+check_len])
            if check_num <= int(p):
                check_cnt += 1
                answer = check_cnt
                
        
    return answer