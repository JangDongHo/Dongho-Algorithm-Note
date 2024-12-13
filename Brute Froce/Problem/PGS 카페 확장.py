# https://school.programmers.co.kr/learn/courses/15009/lessons/121689

from collections import deque

def solution(menus, orders, k):
    orders = deque(orders)
    waits = deque()
    cnt = 0
    
    for t in range(k * len(orders) + 1):
        # 1. 음료 제작 및 나가는 손님 퇴장
        if waits:
            waits[0] -= 1
            if waits[0] == 0:
                waits.popleft()
        # 2. 들어오는 손님 입장
        if orders and t % k == 0:
            waits.append(menus[orders.popleft()])
        # 3. 대기 손님 수 카운팅
        cnt = max(cnt, len(waits))
    
    return cnt