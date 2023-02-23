# 개인정보 수집 유효기간
# 2023 kakao blind recruitment
# 2023.02.15
# 15:00 ~ 15:50 (50 min)
# 후기 : 연도, 월, 일을 하나의 정수(일자)로 접근하여 오늘날짜에 대한 각 유효기간을 계산적으로 처리하면 되는 문제. 처음에 문제 접근을 잘못하여 시간이 다소 걸림. 


def solution(today, terms, privacies):
    data = []
    c_type = []
    data_dict = {}
    today_num = today.split('.')
    today_num = int(today_num[2]) + 28*int(today_num[1]) + 12*28*int(today_num[0])
 
    terms_type = []
    terms_m = []
    privacies_type = []
    privacies_m = []
    pri_num1 = []
    terms_num = 0
    pri_num = 0
    pri_check = 0
    
    answer = []
    for i in range(len(terms)):
        terms_split = terms[i].split(' ')
        
        terms_type.append(terms_split[0])
        terms_num = int(terms_split[1])*28
        terms_m.append(terms_num)
    
    for i in range(len(privacies)):
        privacies_split = privacies[i].split(' ')
        pri_num1 = privacies_split[0].split('.')
        pri_num = int(pri_num1[2]) + 28*int(pri_num1[1]) + 12*28*int(pri_num1[0])
        
        privacies_type.append(privacies_split[1])
        
        privacies_m.append(pri_num)
        
    for i in range(len(privacies_m)):
        for j in range(len(terms_type)):
       
            if privacies_type[i] == terms_type[j]:
                
                pri_check = terms_m[j] + privacies_m[i] -1
                if pri_check < today_num:
                    answer.append(i+1)
                
    
    
    return answer

