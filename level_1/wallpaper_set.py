# 바탕화면 정리
# practive problem
# 정답률: 41% 
# 2023.06.29
# 13:00 ~ 13:25 (25 min)
# 후기: min, max와 조건문을 활용하는 문제

def solution(wallpaper):
    answer = []
    min_x = 9999
    min_y = 9999
    max_x = 0
    max_y = 0
    
    for i, row in enumerate(wallpaper):
        for j, char in enumerate(str(row)):
            if char == "#":
                if min_x > i:
                    min_x = i
                if min_y > j:
                    min_y = j
                if max_x <= i:
                    max_x = i + 1
                if max_y <= j:
                    max_y = j + 1
    answer.append(min_x)
    answer.append(min_y)
    answer.append(max_x)
    answer.append(max_y)
    return answer