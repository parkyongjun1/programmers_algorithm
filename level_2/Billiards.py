# 당구 연습
# practice problem
# 정답률: 18% 
# 2023.07.10
# 13:30 ~ 14:10 (40 min)
# 후기: 대칭이동을 이용해 조건을 고려해 최솟값을 계산

def solution(m, n, startX, startY, balls):
    answer = []
    for a,b in balls:
        k=10000000
        if startX!=a or b>startY:
            k=min(k,(startX-a)**2+(startY+b)**2)
        if startY!=b or a>startX:
            k=min(k,(startX+a)**2+(startY-b)**2)
        if startX!=a or b<startY:
            k=min(k,(startX-a)**2+(2*n-b-startY)**2)
        if startY!=b or a<startX:
            k=min(k,(2*m-a-startX)**2+(startY-b)**2)
        answer.append(k)
    return answer