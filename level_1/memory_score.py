# 추억 점수
# practive problem
# 정답률: 66% 
# 2023.06.29
# 11:45 ~ 12:00 (15 min)
# 후기: zip을 통해 리스트들을 각각 dict.의 key, value로 선언하면 쉽게 해결되는 문제

def solution(name, yearning, photo):
    answer = []
    yearning_dic = dict(zip(name,yearning))
    score = 0
    for i, name_list in enumerate(photo):
        for j, names in enumerate(name_list):
            if names in yearning_dic:
                score += yearning_dic[names]

        answer.append(score)
        score = 0

    return answer