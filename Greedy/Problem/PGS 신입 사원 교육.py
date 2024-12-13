# https://school.programmers.co.kr/learn/courses/15009/lessons/121688

import heapq

def solution(ability, number):
    # 우선순위 큐 구성
    hq = []
    for n in ability:
        heapq.heappush(hq, n)
    
    # min-heap을 사용해 그리디하게 작은 값 2개씩 선택
    for _ in range(number):
        num1 = heapq.heappop(hq)
        num2 = heapq.heappop(hq)
        sum_num = num1 + num2
        heapq.heappush(hq, sum_num)
        heapq.heappush(hq, sum_num)
    
    return sum(hq)