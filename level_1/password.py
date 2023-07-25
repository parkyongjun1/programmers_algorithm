# 둘만의 암호
# practive problem
# 정답률: 51% 
# 2023.07.25
# 19:00 ~ 20:00 (60 min)
# 후기: 기본 pipeline을 잡고 코딩하는 것은 금방 했지만, 
#      index가 기존 알파벳 리스트에 벗어나는것을 생각해야하는 것을 찾는데 시간이 다소 걸렸다.


def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    alpha = list(str(alpha))
    skip_list = list(str(skip))
    trans = []
    idx = 0
    
    for i in skip_list:
        if i in alpha:
            alpha.remove(i)
    
    for i in s:
        idx = alpha.index(i)
        if len(alpha) <= index:
            index = index%len(alpha)
            if idx+index >= len(alpha):
                idx = idx-len(alpha)
        elif idx+index >= len(alpha):
            idx = idx-len(alpha)
        answer += alpha[idx+index]
    
    
    return answer