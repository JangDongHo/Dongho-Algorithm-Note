# https://school.programmers.co.kr/learn/courses/15008/lessons/121685

def dfs(n, p):
    # Base Case
    if n == 1:
        return "Rr"
    
    # Recursive Case
    parent_idx = (p - 1) // 4 + 1 # 1-index
    parent = dfs(n - 1, parent_idx) # 부모의 형질 계산
    child_idx = (p - 1) % 4 # 부모의 자식 중 몇 번째인지 계산
    
    if parent == "RR":
        return "RR"
    elif parent == "rr":
        return "rr"
    else:  # parent == "Rr"
        return ["RR", "Rr", "Rr", "rr"][child_idx]
    

def solution(queries):
    result = []
    
    for query in queries:
        result.append(dfs(query[0], query[1]))
    
    return result
    