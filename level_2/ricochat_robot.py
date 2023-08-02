# 리코쳇 로봇
# practice problem
# 정답률: 38% 
# 2023.08.02
# 14:30 ~ 16:10 (100 min)
# 후기: bfs를 이용해 해결하는 문제로, board길이 만큼 count 리스트를 만들고, 로봇이 상하좌우로 벽이나 장애물을 만나기
#      전까지 이동한 후 현재 카운트 값을 고려해준다. 만약 goal 위치인 end 카운트가 INF가 아닐때 리턴해준다.

from collections import deque
DIRS = ((-1,0),(1,0),(0,-1),(0,1))
INF = float('inf')

def solution(board):
    MAX_R, MAX_C = len(board), len(board[0])
    start, end = [0,0], [0,0]
    
    for r in range(MAX_R):
        for c in range(MAX_C):
            if board[r][c] == 'R':
                start = [r,c]
            elif board[r][c] == 'G':
                end = [r,c]
    start_r, start_c = start
    end_r, end_c = end
    counts = [[INF]* MAX_C for _ in range(MAX_R)]
    counts[start_r][start_c] = 0
    dq = deque([[start_r,start_c,counts[start_r][start_c]]])
    
    while dq:
        if counts[end_r][end_c] != INF:
            return counts[end_r][end_c]
        
        curr_r, curr_c, curr_count = dq.popleft()
        
        for dir_r, dir_c in DIRS:
            post_r, post_c, post_count = curr_r, curr_c, curr_count+1
            
            while 0<=post_r + dir_r <MAX_R and 0<=post_c + dir_c < MAX_C and board[post_r+dir_r][post_c+dir_c] != 'D':
                post_r, post_c = post_r+dir_r, post_c+dir_c
            if post_count < counts[post_r][post_c]:
                counts[post_r][post_c] = post_count
                dq.append([post_r, post_c, post_count])
                
    return -1