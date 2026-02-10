# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    main_queue, sub_queue = deque(queue1), deque(queue2)
    total = sum(main_queue + sub_queue)

    if total % 2 == 1:
        return -1
    
    target = total // 2
    # 200만 번 그리디하게 시뮬레이션 수행
    main_sum = sum(main_queue)
    for cnt in range(0, int(2e6)):
        if main_sum == target:
            return cnt
        if main_sum < target:
            val = sub_queue.popleft()
            main_queue.append(val)
            main_sum += val
        else:
            val = main_queue.popleft()
            sub_queue.append(val)
            main_sum -= val
    
    return -1
            
    
    