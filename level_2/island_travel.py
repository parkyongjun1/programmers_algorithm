# 명예의전당1
# practice problem
# 정답률: 48% 
# 2023.08.14
# 16:20 ~ 15:30 (70 min)
# 후기: dfs를 이용해 문제를 해결, 초반 dfs 함수 설계를 잘못해서 시간이 다소 걸림.



import sys
from collections import deque
sys.setrecursionlimit(10000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(maps):
    def dfs(x,y) -> int:
        ret = 0
        if x<0 or y<0 or x>=col or y>=row:
            return ret
        if maps[x][y] != 'X' and vis[x][y] is False:
            vis[x][y] = True
            for i in range(4):
                ret += dfs(x+dx[i],y+dy[i])
            return int(maps[x][y]) + ret
        return ret

    ans = []
    col = len(maps)
    row = len(maps[0])
    vis = [[False for i in range(row)] for j in range(col)]

    for i in range(col):
        for j in range(row):
            if maps[i][j] != 'X' and vis[i][j] is False:
                ans.append(dfs(i, j))
    if len(ans) == 0:
        return [-1]
    return sorted(ans)

