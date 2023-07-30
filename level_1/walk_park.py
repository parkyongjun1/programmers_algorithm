# 공원 산책
# practice problem
# 정답률: 37% 
# 2023.06.28
# 10:00 ~ 11:20 (80 min)
# 후기: 조건문을 이용한 문제로 난이도는 어렵지 않았지만 복잡도를 개선을 위해 다소 시간이 많이 걸림.

def solution(park, routes):
    answer = []
    str_park = []
    park_mod_row = len(str(park[0]))
    park_mod_col = len(park)
    
    for i in range(len(park)):
            for j in range(len(str(park[i]))):
                str_park.append(str(park[i])[j])
    for i in range(len(str_park)):
        if str_park[i] == "S":
            str_p = i
            break
            
    for i in routes:
        Compose, loc = i.split(" ")
        loc = int(loc)
        if Compose == "E":
            if str_p % park_mod_row + loc >= park_mod_row:
                continue
            park_result = str_p
            
            for j in range(1,loc+1):    
                str_p = str_p + 1
                if str_park[str_p] == "X":
                    str_p = park_result
                    break
                 
        elif Compose == "W":
            if str_p % park_mod_row - loc < 0:
                continue
            park_result = str_p
            
            for j in range(1,loc+1):    
                str_p = str_p - 1
                if str_park[str_p] == "X":
                    str_p = park_result
                    break
        
        elif Compose == "S":
            if str_p//park_mod_row + loc >= park_mod_col:
                continue
            park_result = str_p
        
    
            for j in range(1, loc+1):    
                str_p = str_p + park_mod_row
                
                if str_park[str_p] == "X":
                    str_p = park_result
                    break
             
        if Compose == "N":
            if str_p//park_mod_row - loc < 0:
                continue
            park_result = str_p
            
            for j in range(1, loc+1):    
                str_p = str_p - park_mod_row
                if str_park[str_p] == "X":
                    str_p = park_result
                    break
    answer.append(str_p//park_mod_row)
    answer.append(str_p%park_mod_row)
    return answer