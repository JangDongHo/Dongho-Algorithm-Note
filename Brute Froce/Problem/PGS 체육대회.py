# https://school.programmers.co.kr/learn/courses/15008/lessons/121684

from itertools import permutations

def solution(ability):
    n = len(ability) # 학생 수
    m = len(ability[0]) # 종목 수
    ans = 0
    
    # 모든 가능한 경우의 수를 계산 (순열)
    for person_idxs in permutations(range(n), m):
        tmp = 0
        for s_idx, p_idx in enumerate(person_idxs):
             tmp += ability[p_idx][s_idx]
        ans = max(ans, tmp)
        
    return ans