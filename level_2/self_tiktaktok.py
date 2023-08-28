# 혼자서하는 틱택토
# practice problem
# 정답률: 34% 
# 2023.08.28
# 15:00 ~ 16:20 ( 80 min)
# 후기: 빙고가 완성되는 16가지 경우의 수를 구한 후 게임의 규칙에 따라 조건을 고려해서 문제를 해결.

def solution(board):
    answer = -1
    cnt_o = 0
    cnt_x = 0
    comp_o = 0
    comp_x = 0
    
    for i in board:
        cnt_o += i.count('O')
        cnt_x += i.count('X')
   
    for i in range(3):
        for j in range(3):
            if i == 0 and j == 0:
                if board[i][j] == 'O' and board[i][j+1] == 'O' and board[i][j+2] == 'O':
                    comp_o += 1
                if board[i][j] == 'X'and board[i][j+1] == 'X'and board[i][j+2] == 'X':
                    comp_x += 1
                if board[i][j]  == 'O'and board[i+1][j] == 'O' and board[i+2][j] == 'O':
                    comp_o += 1
                if board[i][j] == 'X'and board[i+1][j] == 'X'and board[i+2][j] == 'X':
                    comp_x += 1
                if board[i][j]  == 'O'and board[i+1][j+1]  == 'O'and board[i+2][j+2] == 'O':
                    comp_o += 1
                if board[i][j] == 'X'and board[i+1][j+1] == 'X'and board[i+2][j+2] == 'X':
                    comp_x += 1
            if i == 0 and j == 1:
                if board[i][j] == 'O' and board[i+1][j] == 'O' and board[i+2][j] == 'O':
                    comp_o += 1
                if board[i][j]== 'X' and board[i+1][j]== 'X' and board[i+2][j] == 'X':
                    comp_x += 1
            if i == 0 and j == 2:
                if board[i][j] == 'O' and board[i+1][j] == 'O' and board[i+2][j] == 'O':
                    comp_o += 1
                if board[i][j]== 'X' and board[i+1][j]== 'X' and board[i+2][j] == 'X':
                    comp_x += 1
                if board[i][j] == 'O' and board[i+1][j-1] == 'O' and board[i+2][j-2] == 'O':
                    comp_o += 1
                if board[i][j]== 'X' and board[i+1][j-1]== 'X' and board[i+2][j-2] == 'X':
                    comp_x += 1
                    
            if i == 1 and j == 0:
                if board[i][j] == 'O' and board[i][j+1] == 'O' and board[i][j+2] == 'O':
                    comp_o += 1
                if board[i][j]== 'X' and board[i][j+1]== 'X' and board[i][j+2] == 'X':
                    comp_x += 1
            if i == 2 and j == 0:
                if board[i][j] == 'O' and board[i][j+1] == 'O' and board[i][j+2] == 'O':
                    comp_o += 1
                if board[i][j]== 'X' and board[i][j+1]== 'X' and board[i][j+2] == 'X':
                    comp_x += 1
    answer = 1
    
    if cnt_o < cnt_x:
        answer = 0
    if comp_o ==0 and comp_x ==0 and cnt_o > cnt_x:
        if cnt_o != cnt_x + 1:
            answer = 0
    if comp_o != 0:
        if comp_x > 0:
            answer = 0
        else:
            if cnt_x != cnt_o -1:
                answer = 0
    if comp_x != 0:
        if comp_o >0:
            answer =0
        else:
            if cnt_x != cnt_o:
                answer = 0           
                    
    return answer