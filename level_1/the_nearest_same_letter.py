# 가장 가까운 같은 글자
# practive problem
# 정답률: 61% 
# 2023.02.15
# 14:05 ~ 14:20 (20 min)
# 후기: reverse 함수를 통해 어렵지 않게 해결할 수 있었음.

def solution(s):
    answer = []
    answer_check = []
    for i in range(len(s)):
        answer.append(-1)
        answer_check.append(-1)
    for i in range(len(s)):
        if i == 0:
            pass
        else:
            for j in reversed(range(len(s[:i]))):
                
                if s[j] == s[i]:
                    answer[i] = i-j
                    answer_check[i] = answer[i]
                    break
                   
                else:
                    continue
            
    return answer