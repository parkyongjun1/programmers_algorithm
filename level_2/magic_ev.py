# 마법의 엘리베이터
# practice problem
# 정답률: 46% 
# 2023.11.01
# 15:00 ~ 16:00 (60 min)
# 후기: 현재 인덱스의 숫자가 5이상인지를 판단하여 올림 또는 내림으로 접근함.
#      하지만 현재 숫자가 5일때 다음 자릿수가 5이상인지 아닌지에 따라 올림, 내림 유무를 결정해야 하는 것을 알아내는데 시간이 다소 걸림. 

def solution(storey):
    answer = 0
    str_storey = str(storey)[::-1]
    chk_num = False
    present_num = 0
    
    for i in range(len(str_storey)):
        present_num = int(str_storey[i])
        
        if chk_num == True:
            present_num += 1
        
        chk_num = False
        
        if present_num<5:
            
            answer += present_num
            
        elif present_num == 5:
            if i < len(str_storey)-2:
                if int(str_storey[i+1])>=5:
                    answer += 10-present_num
                    chk_num = True
                else:
                    answer += present_num
            else:
                answer += present_num
                    
        else:
            answer += 10-present_num
            chk_num = True
            if i == len(str_storey)-1:
                answer += 1
    return answer