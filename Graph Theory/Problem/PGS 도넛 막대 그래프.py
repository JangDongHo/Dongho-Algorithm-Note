# https://school.programmers.co.kr/learn/courses/30/lessons/258711

MAX = int(1e6)

def solution(edges):
    in_degree = [0] * (MAX + 1) # in_degree[x]: 노드 x로 들어오는 간선의 개수
    out_degree = [0] * (MAX + 1) # out_degree[x]: 노드 x에서 나가는 간선의 개수
    
    for a, b in edges:
        out_degree[a] += 1
        in_degree[b] += 1
    
    total = 0 # 전체 그래프 개수
    ans = [-1, 0, 0, 0] # (추가된 노드, 도넛 개수, 막대 개수, 8자 개수)
    for i in range(1, MAX + 1):
        if in_degree[i] == 0 and out_degree[i] == 0:
            continue
        
        # 8자 모양 그래프
        if in_degree[i] >= 2 and out_degree[i] == 2:
            ans[3] += 1
        
        # 막대 모양 그래프
        elif out_degree[i] == 0:
            ans[2] += 1
        
        # 추가된 노드
        elif in_degree[i] == 0 and out_degree[i] >= 2:
            ans[0] = i
            total = out_degree[i]
        
    # 도넛 모양 그래프
    ans[1] = total - (ans[2] + ans[3])
    
    return ans
    