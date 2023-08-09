# 기사단원의 무기
# practice problem
# 정답률: 59% 
# 2023.08.09
# 17:10 ~ 17:40 (30 min)
# 후기: for 문을 이용하여 나머지로 약수의 개수를 count했지만, n까지 보는 문제로 시간초과가 걸림.
#      이후 제곱근을 이용해 25에서 5와 같이 제곱의 수가 같을때에 count를 1로 세고, 나머지는 2로 세서 해결함. 

def solution(number, limit, power):
    answer = 0
    cnt = 0
    total_iron = 0
    for i in range(1, number+1):
        for j in range(1,int(i**(1/2))+1):
            if i % j == 0:
                cnt += 2
                if j**2 == i:
                    cnt -= 1
                
        
        if cnt > limit:
            cnt = power
        
        total_iron += cnt
        cnt = 0
        
    return total_iron