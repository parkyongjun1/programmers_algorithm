# 콜라문제
# practice problem
# 정답률: 68% 
# 2023.10.01
# 09:00 ~ 09:20 (20 min)
# 후기: 교환가능한 개수의 몫을 이용해 문제를 해결함. 나누어 떨어지지 않는 나머지를 더해주면서 while문을 돌려 해결함.


def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n//a) * b
        
        if n%a != 0:
            n = (n//a)*b + (n%a)    
        else:
            n = (n//a)*b
        
    
    return answer