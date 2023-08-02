# 정수 삼각형
# practice problem
# 정답률: 60% 
# 2023.08.02
# 17:00 ~ 18:00 (60 min)
# 후기: 그래프 노드의 대각값을 이용해 값을 더해나가는 식으로 문제를 해결


def solution(triangle):
    
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1,n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j]+dp[i-1][j]
            elif i == j:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1],dp[i-1][j])
            
    return max(dp[-1])