# 대충 만든 자판
# practice problem
# 정답률: 51% 
# 2023.07.24
# 14:50 ~ 15:50 (60 min)
# 후기: keymap의 알파벳을 dict의 k로 주고 idx를 value로 선언하여 문제를 해결, 
#      처음에 zip을 사용하지 않고 시도하느라 시간이 오래 걸림.



def solution(keymap, targets):
    answer = []
    keys = []
    keys_idx = []
    cnt = 0

    for i in keymap:
        for idx1, key in enumerate(i):
            if key not in keys:
                keys.append(key)
                keys_idx.append(idx1)
            if key in keys:
                chg_idx = keys.index(key)
                if keys_idx[chg_idx] > idx1:
                    keys_idx[chg_idx] = idx1

        alpa_dict = dict(zip(keys,keys_idx))
    
    for i in targets:
        for j in i:
            if j in alpa_dict:
                cnt += alpa_dict[j]+1
            if j not in alpa_dict:
                cnt = -1
                break
        answer.append(cnt)
        cnt = 0
    return answer