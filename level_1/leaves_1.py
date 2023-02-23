# 나머지가 1이 되는 수 찾기
# 월간 코드 챌린지 시즌3
# 2023.02.23
# 11:15 ~ 11:26 (11 min)
# 후기 : 처음에 문제를 이해할때 x가 3이상이라 착각해 시간이 다소 걸림. 문제 자체는 쉬웠음.


def solution(n):
    answer = 0
    for i in range(1,n):
        if n % i == 1:
            answer = i
            break
            
    return answer