# 호텔 대실
# practice problem
# 정답률: 46% 
# 2023.09.05
# 10:10 ~ 11:40 (90 min)
# 후기: deque를 이용해 겹치지 않는 시간을 고려해 문제를 해결함. 풀이 중간에 deque의 시간 정렬을 하지 않고, 풀이를 하다 시간이 다소 오래걸렸다. 

from collections import deque

def solution(book_time):
    answer = 0
    book_time.sort(key= lambda x:x[0])
    room_time = []
    room_list = []
    cnt = 0
    
   
    for idx, i in enumerate(book_time):
        room_time = []
        start, end = i
        start = start.split(':')
        end = end.split(':')
        start = int(start[0])*60 + int(start[1])
        end = int(end[0])*60 + int(end[1])
        room_time.append(start)
        room_time.append(end)
        room_list.append(room_time)
        if idx==0:
            dq = deque([[start,end]])
            
        else:
            while dq:
                start_ch, end_ch = dq.popleft()
                if end_ch + 10 <= start:
                    dq.append([start,end])
                    dq = deque(sorted(dq,key= lambda x:x[1]))
                    break
                else:
                    dq.append([start_ch,end_ch])
                    dq.append([start,end])
                    dq = deque(sorted(dq,key= lambda x:x[1]))
                    break
                 
        answer = len(dq)
    return answer