# 삼총사
# practice problem
# 정답률: 72% 
# 2023.10.01
# 15:00 ~ 16:00 (60 min)
# 후기: 처음 정수 숫자가 중복된다는 점을 캐치못해 중복없는 조건으로 코드를 작성했다. 
#      이후 중복된다는 점을 캐치하고 3중 for문을 사용해 모든 조합을 고려해 문제를 해결했다.


def solution(number):
    sum_n = 0
    cnt = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1,len(number)):
                sum_n = number[i] + number[j] + number[k]
                if sum_n == 0:
                    cnt += 1
        sum_n = 0

    return cnt