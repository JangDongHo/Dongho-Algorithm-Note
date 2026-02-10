# https://school.programmers.co.kr/learn/courses/30/lessons/258707

def solution(coin, cards):
    n = len(cards)
    pair = [-1] * n
    cost = [-1] * n
    
    # 짝 정보(pair) 갱신 - O(n^2)
    for b in range(n - 1, -1, -1):
        if pair[b] != -1: continue
        for a in range(b):
            if cards[a] + cards[b] == n + 1:
                cost[b] = 2
                pair[a] = b
                pair[b] = a
    
    # 처음 n/3 장의 카드와 짝인 카드의 cost를 깎아주기 - O(n)
    for i in range(n // 3):
        if i < pair[i]:
            cost[pair[i]] -= 1
        else:
            cost[i] -= 1
    
    # 카드 선택 반복 탐색 - O(n^2)
    visited = [False] * n
    pair_cnt = 0
    while coin >= 0:
        max_idx = n // 3 + 2 * (pair_cnt + 1) - 1
        max_idx = min(max_idx, n - 1) # 범위를 벗어나지 않게 예외 처리
        
        best_idx = -1
        for idx in range(max_idx + 1):
            if visited[idx] or idx < pair[idx]: # 이미 고른 카드거나, 쌍보다 앞에 있는 카드라면
                continue
            if best_idx == -1 or cost[idx] < cost[best_idx]: # 더 싼 값으로 카드 쌍을 만들 수 있다면 갱신
                best_idx = idx
        
        if best_idx == -1 or coin - cost[best_idx] < 0: # 모든 카드를 골랐거나, 카드를 살 수 없다면
            break
        
        coin -= cost[best_idx]
        visited[best_idx] = True
        pair_cnt += 1
    
    return min(pair_cnt + 1, n // 3 + 1) # n // 3 + 1은 최대로 나올 수 있는 라운드를 의미