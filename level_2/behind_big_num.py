# 명예의전당1
# practice problem
# 정답률: 57% 
# 2023.08.17
# 16:10 ~ 17:15 (65 min)
# 후기: 처음에 dp로 방문했는지의 여부로 접근했지만, 이후 stack 개념으로 다시 접근함.

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:            
            answer[stack.pop()] = number

        stack.append(idx)
    return answer
    