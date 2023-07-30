# 과제 진행하기
# practice problem
# 정답률: 35% 
# 2023.07.30
# 14:10 ~ 15:25 (75 min)
# 후기: 처음 접근을 바로 작업이 가능한 과제를 뽑고, 이후 나머지를 역순으로 더하는 접근을 했지만,
#      남은 시간에 대해서 이전 작업들이 완료될 수 있다는 점을 다시 고려해 문제를 해결함.


from collections import deque


def solution(plans):
    def get_time(time):
        hour, minute = int(time[0:2]), int(time[3:5])
        return hour * 60 + minute

    plans = sorted(list(
        map(lambda x: [x[0], get_time(x[1]), int(x[2])], plans)), key=lambda x: x[1])
    answer, wait, now = [], deque([plans[0]]), plans[0][1]

    for i, v in enumerate(plans[1:]):
        next_time = v[1]

        while wait:
            j, t, q = wait.pop()
            if t > now:
                now = t
            lest = now + q

            if lest <= next_time:
                now += q
                answer.append(j)
            else:
                now = next_time
                wait.append([j, t, lest - next_time])
                break

        wait.append(v)

    while wait:
        answer.append(wait.pop()[0])

    return answer