# 시소짝궁
# practice problem
# 정답률: 45% 
# 2023.10.11
# 14:45 ~ 15:30 (45 min)
# 후기: 처음 문제해결 접근방식을 2중 for문으로 설계했지만, 시간초과 문제를 겪음.
#      이후 Counter 함수를 이용해 dic. 형식으로 문제를 해결함.

from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    for i in range(100,1001):
        if counter[i] > 0:
            answer += counter[i]*((counter[i]-1)/2)
            answer += counter[i]*counter[i*(3/2)]
            answer += counter[i]*counter[i*2]
            answer += counter[i]*counter[i*(4/3)]
    return answer