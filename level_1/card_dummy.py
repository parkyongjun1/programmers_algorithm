# 카드 뭉ㅣ
# practive problem
# 정답률: 62% 
# 2023.07.27
# 17:00 ~ 17:50 (50 min)
# 후기: 처음에 접근은 reverse로 고려해 문제를 풀다 시간이 오래 걸렸다.
#      다시 순방향으로 접근해 바로 문제를 해결함.


def solution(cards1, cards2, goal):
    answer = ''
    word_check = goal.copy()
    
    for i in word_check:
        if i in cards1:
            if cards1.index(i) == 0:
                cards1.remove(i)
                goal.remove(i)
                
        elif i in cards2:
            if cards2.index(i) ==0:
                cards2.remove(i)
                goal.remove(i)
    
    if len(goal) == 0:
        answer = 'Yes'
        
    else:
        answer = 'No'
            
    return answer
