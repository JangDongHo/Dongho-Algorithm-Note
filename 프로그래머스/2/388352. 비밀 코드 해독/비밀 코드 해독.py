from itertools import combinations

def count_same(arr1, arr2):
    count = 0
    
    for num1 in arr1:
        if num1 in arr2:
            count += 1

    return count

def solution(n, q, ans):
    answer = 0
    
    # 1부터 n까지의 서로 다른 정수 5개 모두 탐색 (nC5
    comb = combinations(range(1, n+1), 5)
    
    for t1 in comb:
        is_success = True
        
        for (i, t2) in enumerate(q):
            if count_same(t1, t2) != ans[i]:
                is_success = False
                break
        
        if is_success:
            answer += 1

    return answer