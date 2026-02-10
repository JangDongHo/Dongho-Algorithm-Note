# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq
from collections import defaultdict


def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙 (음수로 저장)
    entry_map = defaultdict(int)  # 실제 존재하는 값 관리

    for op in operations:
        if op == "D 1":  # 최댓값 삭제
            while max_heap:
                max_val = -heapq.heappop(max_heap)
                if entry_map[max_val] > 0:  # 유효한 값인지 확인
                    entry_map[max_val] -= 1
                    break
        elif op == "D -1":  # 최솟값 삭제
            while min_heap:
                min_val = heapq.heappop(min_heap)
                if entry_map[min_val] > 0:  # 유효한 값인지 확인
                    entry_map[min_val] -= 1
                    break
        else:
            num = int(op.split()[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_map[num] += 1

    # 남아있는 값 정리 (유효한 최댓값/최솟값 찾기)
    while min_heap and entry_map[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_map[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    # 결과 출력
    if not min_heap or not max_heap:
        return [0, 0]

    return [-max_heap[0], min_heap[0]]
