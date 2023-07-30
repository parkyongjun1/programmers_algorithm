# 광물 캐기
# practice problem
# 정답률: 39% 
# 2023.07.24
# 12:50 ~ 14:20 (90 min)
# 후기: 광물의 집합을 5개 단위 리스트로 만든 뒤 우선순위를 dia,iron,stone만 고려했을때 테스트케이스 8번이 자꾸 오류가 났다. 
#      조건 중 광물의 순서는 변경 불가하기때문에 곡괭이의 수가 광물 집합보다 작은 경우 슬라이싱 처리를 해야하는 것을 찾는데 시간이 다소 걸렸다.


def solution(picks, minerals):
    mineral_list=[]
    total_list =[]
    tired = 0
    dia_num = picks[0]
    iron_num = picks[1]
    stone_num = picks[2]
    total_num = dia_num + iron_num + stone_num
    for idx, i in enumerate(minerals):
        if idx != 0 and idx % 5 == 0:
            total_list.append(mineral_list)
            mineral_list = []
            
        mineral_list.append(i)
        if idx == len(minerals)-1:
            total_list.append(mineral_list)
    
    # 곡괭이 수가 광물의 집합의 수가 같거나 클때
    if len(total_list) <= total_num:
        total_list.sort(key = lambda x:(-x.count('diamond'),-x.count('iron'),-x.count('stone')))
    
    # 곡괭이 수가 광물의 집합의 수보다 작을때
    elif len(total_list) > total_num:
        total_list = total_list[:total_num]
        total_list.sort(key = lambda x:(-x.count('diamond'),-x.count('iron'),-x.count('stone')))
    
    
    for i in total_list:
        for idx, j in enumerate(i):
            if dia_num > 0:
                tired += 1
                
                if idx == len(i)-1:
                    dia_num -= 1
                  
            elif dia_num == 0 and iron_num >0:
                if j == 'diamond':
                    tired += 5
                    
                elif j == 'iron' or 'stone':
                    tired += 1
                    
                if idx == len(i)-1:
                    iron_num -= 1
                 
            elif dia_num ==0 and iron_num ==0 and stone_num >0:
                if j == 'diamond':
                    tired += 25
                    
                elif j == 'iron':
                    tired += 5
                    
                elif j == 'stone':
                    tired += 1
                    
                if idx == len(i)-1:
                    stone_num -= 1
            if dia_num == 0 and iron_num == 0 and stone_num ==0:
                break
    
    return tired