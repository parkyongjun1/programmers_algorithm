# 신고 결과 받기
# 2022 KAKAO BLIND RECRUITMENT
# 정답률: 34% 
# 2023.03.06
# 15:30 ~ 16:45 (75 min)
# 후기: 문제를 이해하고 O(2N)으로 코드를 짜는 데는 40분정도 걸렸지만, report의 n 때문에 시간초과 문제를 해결하는데 추가적으로 시간이 오래 걸렸다. 결국 set을 이용해 O(N)을 줄이는 것이 중요함.


def solution(id_list, report, k):
    answer = []
    report_cnt = dict.fromkeys(id_list,0)
    report_final_cnt = dict.fromkeys(id_list,0)
    report_list = []
    union_report = set(report)
    
    for i in union_report:    
        report_cnt[i.split()[1]] += 1
        if report_cnt[i.split()[1]] >= k:
            if i.split()[1] not in report_list:
                report_list.append(i.split()[1])
                    
            
    for i in union_report:
        if i.split()[1] in report_list:
            report_final_cnt[i.split()[0]] +=1
    answer = list(report_final_cnt.values())
        
    return answer