# https://school.programmers.co.kr/learn/courses/30/lessons/72411

## 풀이 1. 모든 코스 조합을 완전 탐색하는 방법 (딕셔너리 자료구조 사용)

from itertools import combinations

def solution(orders, courses):
    dictionary = {}
    ans = []
    
    # orders 처리
    for order in orders:
        for i in range(2, len(order) + 1):
            if i not in dictionary:
                dictionary[i] = {}
            for comb_list in combinations(order, i):
                comb_list = sorted(comb_list)
                comb_str = "".join(comb_list)
                if comb_str in dictionary[i]:
                    dictionary[i][comb_str] += 1
                else:
                    dictionary[i][comb_str] = 1
    
    # courses를 순회하며 결과 추출
    for course_len in courses:
        if course_len in dictionary:  # 해당 길이의 조합이 있을 경우
            max_count = max(dictionary[course_len].values(), default=0)  # 최대 주문 횟수
            if max_count >= 2:  # 최소 2명 이상 주문된 경우만
                ans.extend(
                    [menu for menu, count in dictionary[course_len].items() if count == max_count]
                )

    return sorted(ans)  # 결과를 사전순 정렬 후 반환
    
## 풀이 2. 모든 코스 조합을 완전 탐색하는 방법 (Counter 클래스 사용)
from collections import Counter
from itertools import combinations

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)
        most_ordered = Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
    return [''.join(v) for v in sorted(result)]