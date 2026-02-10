# https://school.programmers.co.kr/learn/courses/30/lessons/92342

from itertools import combinations_with_replacement

def compare_score(apeach, lion):
    lion_point = 0
    apeach_point = 0
    
    for i in range(11):
        if lion[i] == 0 and apeach[i] == 0:
            continue
        elif lion[i] <= apeach[i]:
            apeach_point += 10 - i
        else:
            lion_point += 10 - i
    
    return lion_point - apeach_point

def solution(n, info):
    best_point = 0
    best_result = [0] * 11
    
    for comb in combinations_with_replacement(range(11), n):
        cur_result = [0] * 11
        
        for num in comb:
            cur_result[num] += 1
        
        cur_point = compare_score(info, cur_result)
        
        if (cur_point > best_point) or (cur_point == best_point and cur_result[::-1] > best_result[::-1]):
            best_point = cur_point
            best_result = cur_result
    
    return [-1] if best_point == 0 else best_result