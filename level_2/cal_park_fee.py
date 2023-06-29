# 주차 요금 계산
# 2022 KAKAO BLIND RECRUITMENT
# 정답률: 57% 
# 2023.06.27
# 12:50 ~ 14:30 (100 min)
# 후기: dict.를 활용해 문제 조건에 부합하게 문제를 해결. 다양한 조건에 맞게 문제를 하나하나 해결함. 문제 자체의 난이도는 보통이지만, 차근차근 조건에 맞게 짜는데 시간이 걸림.

import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    car_num= []
    car_info = {}
    car_result = {}
    car_check = {}
    car_fee = {}
    base_check = 0
    
    for idx, i in enumerate(records):
        times, number, c= i.split()
        hours, minutes = times.split(":")
        if c=="IN":
            car_info[number] = times
            car_check[number] = times
            
        if c=="OUT":
            time = int(hours)*60 + int(minutes) - int(car_info[number].split(":")[0])*60 - int(car_info[number].split(":")[1])
            
            if number in car_result.keys():
                a = car_result[number] + time
                car_result[number] = a
            else:
                car_result[number] = time
            
            del(car_check[number])
            
            base_check = int(car_result[number])-fees[0]
            if base_check <= 0:
                extra = 0
            else:
                extra = int(car_result[number])-fees[0]
            car_fee[number] = fees[1] + (math.ceil(extra/fees[2])) * fees[3]
            
        # if idx == len(records) - 1:
    if car_check is not None:
        for j in car_check:
            time = 23*60 + 59 - int(car_check[j].split(":")[0])*60 - int(car_check[j].split(":")[1])

            if len(car_result) != 0:
                a = car_result[j] + time
                car_result[j] = a
            else:
                car_result[j] = time

            base_check = int(car_result[j])-fees[0]
            if base_check <= 0:
                extra = 0
            else:
                extra = int(car_result[j])-fees[0]
            car_fee[j] = fees[1] + (math.ceil(extra/fees[2])) * fees[3]
 
    car_fee = sorted(car_fee.items())
    car_fee = dict(car_fee)
    answer = list(car_fee.values())
    
    return answer
