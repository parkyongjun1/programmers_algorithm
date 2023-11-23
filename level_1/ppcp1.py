# PPCP 기출문제 1번
# PPCP
# 정답률:0% 
# 2023.11.23
# 15:30 ~ 16:30 (60 min)
# 후기: 시간상으로 공격을 당했을 때 대미지를 차감해서 문제를 해결. 추가획득되는 체력을 고려하는 부분에서 다소 시간이 걸림.

def solution(bandage, health, attacks):
    answer = 0
    max_time = attacks[-1][0]
    max_health = health
    add_init = False
    add_cnt = 0
    test = []

    for i in range(max_time+1):
        if i == attacks[0][0]:
            add_init = True
            
            health -= attacks[0][1]
            
            if len(attacks)>1:
                attacks = attacks[1:]
    
            elif len(attacks)==1:
                attacks = []
            
            if health <= 0:
                return -1
            
        else:
            if add_init == True:
                add_cnt = 0
                add_init = False
            
            add_cnt += 1
                 
            if health < max_health:
                health += bandage[1]
            
            if add_cnt == bandage[0]:
                health += bandage[2]
                add_cnt = 0
            if health >= max_health:
                health = max_health
        
    return health
