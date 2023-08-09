# 체육복
# practice problem
# 정답률: 55% 
# 2023.08.09
# 17:50 ~ 18:30 (40 min)
# 후기: 문제 자체는 큰 어려움이 없었지만, 초반에 조건 중 lost와 reserve에 동시에 존재하는 경우를 체크하는 점을 빠뜨려
#      다소 시간이 걸렸다.

def solution(n, lost, reserve):
    answer = 0
    cloth_list = []
    cloth_check = 0
    cnt = 0
    
    norm = set(lost).intersection(set(reserve))
    
    for i in range(1,n+1):
        if i in lost and i not in norm:
            cloth_check = 0
            
        elif i in reserve and i not in norm:
            cloth_check = 2
            
        else:
            cloth_check = 1
        
        cloth_list.append(cloth_check)
        cloth_num = cloth_list.copy()
    
    for idx, i in enumerate(cloth_list):
        if idx == 0:
            if i == 2 and cloth_list[idx+1] == 0:
                cloth_list[idx] -= 1
                cloth_list[idx+1] += 1
        
        else:
            if i == 2:
                if cloth_list[idx-1] == 0:
                    cloth_list[idx] -= 1
                    cloth_list[idx-1] += 1
                    
                elif idx != len(cloth_list) -1 and cloth_list[idx+1] ==0:
                    cloth_list[idx] -= 1
                    cloth_list[idx+1] += 1
    
    for i in cloth_list:
        if i != 0:
            cnt += 1
    
    return cnt