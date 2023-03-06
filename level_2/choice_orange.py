# 귤 고르기
# practive problem
# 정답률: 62% 
# 2023.03.06
# 15:45 ~ 16:15 (30 min)
# 후기: 사이즈 별 귤 개수를 내림차순으로 정리하고, 코드를 작성했다. 귤 개수 자체가 k보다 크면 결과를 1로 처리하는 것을 뒤늦게 생각하느라 시간이 조금 걸렸다.

def solution(k, tangerine):
    answer = 0
    set_tangerine = set(tangerine)
    result_num = dict.fromkeys(set_tangerine,0)
    total_cnt = 0
    
    for i in tangerine:
        if i in set_tangerine:
            result_num[i] += 1
    
    sort_num = list(result_num.values())
    sort_num.sort(reverse=True)
    
    for idx, i in enumerate(sort_num):
        if i >= k:
            answer = 1
            break
        if total_cnt < k:
            if total_cnt + i >k:
                answer += 1
                break
            total_cnt += i
            answer += 1
        if total_cnt == k:
             break
        if idx == len(sort_num)-1:
            answer += 1
            
    return answer