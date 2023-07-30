# 달리기 경주
# practice problem
# 정답률: 39% 
# 2023.06.28
# 11:30 ~ 13:00 (90 min)
# 후기: 단순 list를 사용해 코드를 작성하는 것은 금방했지만 list의 index에 따른 시간 복잡도를 해결하지 못해 시간이 오래걸림. dict.를 활용해 시간 복잡도를 해결

def solution(players, callings):
    rankDic = {}
    playerDic = {}
    
    for idx, player in enumerate(players):
        rankDic[idx + 1] = player
        playerDic[player] = idx + 1
    for player_cg in callings:
        cur_rank = playerDic[player_cg]
        prev_rank = cur_rank - 1
        prev_player = rankDic[prev_rank]
        rankDic[cur_rank], rankDic[cur_rank - 1] = rankDic[cur_rank - 1], rankDic[cur_rank]
        playerDic[player_cg], playerDic[prev_player] = playerDic[prev_player], playerDic[player_cg]
    
    return list(rankDic.values())