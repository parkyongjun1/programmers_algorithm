# k진수에서 소수 개수 구하기
# 2022 kakao blind recruitment
# 정답률: 58% 
# 2023.03.08
# 17:45 ~ 18:15 (30 min)
# 후기: 주어진 수를 k진수로 변환하고, 소수인지 체크하는 코드까지는 어렵지 않게 구현하였지만, test time 때 1번 시간초과 문제를 해결하는데 시간이 조금 걸렸다. 방법은 소수인지 판별을 할때 x만큼이 아닌 x의 제곱근까지만 고려해주는 것이 핵심이었다. 


def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(x**(1/2))+1):
        if x%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    rev_base = ''
    n_num = ''
    chk_prime = False
    
    while n > 0:
        rev_base += str(n%k)
        n = n//k
    
    rev_base = rev_base[::-1]
    
    n_num = rev_base.split('0')
  
    for i in n_num:
        if i == '':
            continue
        chk_prime = is_prime(int(i))
        if chk_prime == True:
            answer += 1
        chk_prime = False
    return answer