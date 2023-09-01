# 옹알이2
# practice problem
# 정답률: 57% 
# 2023.09.01
# 13:50 ~ 14:20 (30 min)
# 후기: 발음할 수 있는 단어를 슬라이싱하고, 연속된 경우를 고려해서 발음 가능한 단어를 카운트


def solution(babbling):
    answer = 0
    pron = ['aya','ye','woo','ma']
    word_check = True
    pre_word = ''
    
    for i in babbling:
        while word_check:
            if i[0:3] == 'aya':
                if pre_word == 'aya':
                    break
                pre_word = 'aya'
                i = i[3:]
            elif i[0:2] == 'ye':
                if pre_word == 'ye':
                    break
                pre_word = 'ye'
                i = i[2:]
            elif i[0:3] == 'woo':
                if pre_word == 'woo':
                    break
                pre_word = 'woo'
                i = i[3:]
            elif i[0:2] == 'ma':
                if pre_word == 'ma':
                    break
                pre_word = 'ma'
                i = i[2:]
            else:
                word_check = False
            
        word_check = True
        pre_word = ''
        
        if len(i) == 0:
            answer += 1
        
    return answer