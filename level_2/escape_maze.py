# 미로탈출
# practice problem
# 정답률: 42% 
# 2023.09.03
# 15:30 ~ 17:30 (120 min)
# 후기: 처음 접근을 DFS로 S->L, L->E 두 가지로 돌리니 기본 테스트 케이스에서 시간초과를 겪고, 이후 하나의 while문으로 하는 처리를 했지만, 최종 테스트 케이스에서 실패를 했다.
#      이후 BFS로 접근을 해서 문제를 해결함.

from collections import deque
import copy

DIRS = ((-1,0),(1,0),(0,-1),(0,1))
INF = float('inf')

def solution(maps):
    MAX_R, MAX_C = len(maps), len(maps[0])
    start_1, end_1 = [0,0], [0,0]
    start_2, end_2 = [0,0], [0,0]
    total_count = -1
    
    for r in range(MAX_R):
        for c in range(MAX_C):
            if maps[r][c] == 'S':
                start_1 = [r,c]
            elif maps[r][c] == 'L':
                end_1 = [r,c]
                start_2 = [r,c]
            elif maps[r][c] == 'E':
                end_2 = [r,c]
                
    start_r1, start_c1 = start_1
    start_r2, start_c2 = start_2
    end_r1, end_c1 = end_1
    end_r2, end_c2 = end_2
    counts = [[INF]* MAX_C for _ in range(MAX_R)]
    visited_check = [[False]*MAX_C for _ in range(MAX_R)]
    visited_check2 = copy.deepcopy(visited_check)
    counts_init = copy.deepcopy(counts)
    counts[start_r1][start_c1] = 0
    dq = deque([[start_r1,start_c1,counts[start_r1][start_c1]]])
    check_comp1 = False
    
    while dq:
        curr_r, curr_c, curr_count = dq.popleft()
        visited_check[curr_r][curr_c] == True
        if len(dq)==0 and counts[end_r1][end_c1] != INF and check_comp1 == False:
                total_count = counts[end_r1][end_c1]
                check_comp1 = True
                counts = counts_init
                visited_check = visited_check2
                counts[start_r2][start_c2] = total_count
                dq = deque([[start_r2,start_c2,counts[start_r2][start_c2]]])
                curr_r, curr_c, curr_count = dq.popleft()
                visited_check[curr_r][curr_c] == True
                
        if len(dq)==0 and check_comp1 == True and counts[end_r2][end_c2] != INF:
            return counts[end_r2][end_c2]
            
        for dir_r, dir_c in DIRS:
            post_r, post_c, post_count = curr_r + dir_r, curr_c + dir_c, curr_count + 1
                
            if 0>post_r or post_r >= MAX_R or 0> post_c or post_c >= MAX_C:
                continue
            
            if maps[post_r][post_c] == 'X':
                continue
            if visited_check[post_r][post_c] == True:
                if counts[post_r][post_c] > post_count:
                    dq.append([post_r,post_c,post_count])
                else:
                    continue
            if counts[post_r][post_c] > post_count or counts[post_r][post_c] == INF:
                counts[post_r][post_c] = post_count

            dq.append([post_r, post_c, post_count])
            visited_check[post_r][post_c] = True

    return -1