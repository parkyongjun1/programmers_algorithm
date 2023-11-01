# 큰수 만들기
# practice problem
# 정답률: 50% 
# 2023.10.21
# 13:10 ~ 14:00 (50 min)
# 후기: 슬라이싱을 이용해 큰 수를 구하고, 인덱스를 줄여서 해결함.


def solution(number, k):
    answer = str(number)
    i=0
    
    while i<(len(answer)-1) and k>0:
        if answer[i] < answer[i+1]:
            answer = answer[:i] + answer[i+1:]
            
            if i>0:
                i -= 2
            else:
                i -= 1
            k -= 1    
        i += 1
    if k >0:
        answer = answer[:len(answer)-k]
    
    return answer