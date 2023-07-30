# 연속된 부분 수열의 합
# practice problem
# 정답률: 49% 
# 2023.07.25
# 16:00 ~ 17:00 (60 min)
# 후기: 초반 sequence를 오름차순으로 고려하여 문제를 푸니 시간초과 문제를 겪고, 내림차순으로 문제를 해결함. 
#      idx마다 값을 저장하는 것이 아닌 순차적으로 오버되는 수를 제거하는 식으로 문제를 해결.


def solution(sequence, k):
    answer = []
    summ = 0
    last_index = len(sequence)-1
    
    for i, v in enumerate(sequence[::-1]):
        summ += v
        
        if summ < k:
            pass
        
        elif summ > k:
            summ -= sequence[last_index]
            last_index -= 1
            
            if summ == k:
                answer.append([len(sequence)-1-i, last_index])

        else:
            answer.append([len(sequence)-1-i, last_index])
    
    answer.sort(key=lambda x : (x[1]-x[0], x[0]))
    
    return answer[0]