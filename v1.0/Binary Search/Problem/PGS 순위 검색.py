# https://school.programmers.co.kr/learn/courses/30/lessons/72412
## 풀이 방법: 딕셔너리(해쉬) + 파라매트릭 서치

from collections import defaultdict
from itertools import combinations

def parametric_search(arr, target):
    cur = -1
    steps = len(arr)
    
    while steps != 0:
        while (cur + steps < len(arr)) and (arr[cur + steps] < target):
            cur += steps
        steps //= 2
    
    return cur + 1

def solution(infos, queries):
    dictionary = defaultdict(list)
    ans = []
    
    # 지원자 정보 처리
    for info in infos:
        info = info.split()
        for i in range(5): # 필터링 개수 (0~4개)
            combi = list(combinations(info[:4], i))
            for comb in combi:
                key = " ".join(comb)
                dictionary[key].append(int(info[4]))
    
    # 파라매트릭 서치를 위해 미리 딕셔너리의 value값들 정렬
    for key in dictionary:
        dictionary[key].sort()
    
    # 쿼리문 처리
    for query in queries:
        query = query.replace("and", " ").split()
        q = " ".join([item for item in query[:4] if item != "-"])
        target_score = int(query[4])
        if q in dictionary:
            ans.append(len(dictionary[q]) - parametric_search(dictionary[q], target_score))
        else:
            ans.append(0)
    
    return ans