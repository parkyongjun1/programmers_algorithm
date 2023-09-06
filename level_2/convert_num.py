# 숫자 변환하기
# practice problem
# 정답률: 54% 
# 2023.09.06
# 15:30 ~ 16:20 (50 min)
# 후기: queue를 이용해 연산을 수행하고 연산이 x가 되면 반환해 문제를 해결

def solution(x, y, n):
    answer = -1

    queue=[]
    queue.append([y,0])

    while len(queue)>0:
        now=queue.pop(0)
        if now[0]==x:
            return now[1]
        if now[0]>x:
            if now[0]%3==0:
                queue.append([now[0]//3,now[1]+1])
            if now[0]%2==0:
                queue.append([now[0]//2,now[1]+1])
            queue.append([now[0]-n,now[1]+1])
            
    return answer