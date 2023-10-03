# 숫자짝꿍
# practice problem
# 정답률: 56% 
# 2023.10.03
# 17:00 ~ 18:00 (60 min)
# 후기: 처음 접근을 int, str 변환으로 문제를 해결했지만, 테스트 케이스 11~15번에서 시간초과 문제를 겪고, 
#      해결법을 찾다가 Counter 함수를 통해 0~9까지 Count를 하고 작은 값으로 answer를 구성해 문제를 해결했다.

from collections import Counter

def solution(X, Y):
    answer = ''
    dict_x = {}
    dict_y = {}
    num_chk = ''
    both_num = 0
    
    dict_x = Counter(X)
    dict_y = Counter(Y)
    
    for i in reversed(range(10)):
        num_chk += str(i)
        if dict_x[num_chk] != 0 and dict_y[num_chk] != 0:
            both_num = min(dict_x[num_chk],dict_y[num_chk])
            for j in range(both_num):
                answer += num_chk
        num_chk = ''
        both_num = 0
        
    if len(answer) == 0:
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        return answer