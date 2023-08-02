# 이중순위 우선큐
# practice problem
# 정답률: 60% 
# 2023.08.02
# 16:40 ~ 17:00 (20 min)
# 후기: 현재 operation을 반영한 리스트를 생성해 문제를 해결

import math

def solution(operations):
    answer = []
    max_num = 0
    min_num = 99999
    num_list = []
    
    for i in operations:
        operation, num = i.split(' ')
        if operation == 'I':
            num_list.append(int(num))
        elif operation == 'D':
            if num == '-1':
                if len(num_list) != 0: 
                    num_list.remove(min(num_list))
            elif num == '1':
                if len(num_list) != 0:
                    num_list.remove(max(num_list))
    if len(num_list) == 0:
        answer = [0,0]
    else: 
        answer.append(max(num_list))
        answer.append(min(num_list))
    return answer