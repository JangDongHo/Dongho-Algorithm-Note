# https://school.programmers.co.kr/learn/courses/30/lessons/258709

### 풀이1. 일반적인 DP

from itertools import combinations

def get_A_wins_num(comb_A, comb_B):
    global N, max_score, dice
    
    # dp[n][x]: comb의 n번째 주사위까지 살펴봤을 때, 점수의 합이 x가 나오는 경우의 수
    dp_A = [[0] * (max_score + 1) for _ in range(N + 1)]
    dp_A[0][0] = 1
    
    dp_B = [[0] * (max_score + 1) for _ in range(N + 1)]
    dp_B[0][0] = 1
    
    for n in range(1, N + 1):
        for x in range(1, max_score + 1):
            for num in dice[comb_A[n - 1]]:
                if x - num >= 0:
                    dp_A[n][x] += dp_A[n - 1][x - num]
            
            for num in dice[comb_B[n - 1]]:
                if x - num >= 0:
                    dp_B[n][x] += dp_B[n - 1][x - num]
    
    win_num = 0
    for a in range(1, max_score + 1):
        for b in range(1, a):
            win_num += (dp_A[N][a] * dp_B[N][b])
    
    return win_num
    
    

def solution(_dice):
    global N, max_score, dice
    dice = _dice
    N = len(dice) // 2
    max_score = N * 100
    
    max_wins = -1
    best_comb = []
    for comb_A in combinations(range(N * 2), N):
        comb_B = tuple(num for num in range(N * 2) if num not in comb_A)
        cur_wins = get_A_wins_num(comb_A, comb_B)
        if cur_wins > max_wins:
            max_wins = cur_wins
            best_comb = list(comb_A)
        
    return [bc + 1 for bc in best_comb]

### 풀이2. DP 최적화

from itertools import combinations

def get_A_wins_num(comb_A, comb_B):
    global N, max_score, dice
    
    # dp[n][x]: comb의 n번째 주사위까지 살펴봤을 때, 점수의 합이 x가 나오는 경우의 수
    dp_A = [[0] * (max_score + 1) for _ in range(N + 1)]
    dp_A[0][0] = 1
    
    dp_B = [[0] * (max_score + 1) for _ in range(N + 1)]
    dp_B[0][0] = 1
    
    for n in range(1, N + 1):
        for x in range(1, max_score + 1):
            for num in dice[comb_A[n - 1]]:
                if x - num >= 0:
                    dp_A[n][x] += dp_A[n - 1][x - num]
            
            for num in dice[comb_B[n - 1]]:
                if x - num >= 0:
                    dp_B[n][x] += dp_B[n - 1][x - num]
    
    # 누적합 - O(max_score)
    dp_psum_B = [0] * (max_score + 1)
    for x in range(1, max_score + 1):
        dp_psum_B[x] = dp_B[N][x] + dp_psum_B[x - 1]
    
    win_num = 0
    for x in range(1, max_score + 1):
            win_num += (dp_A[N][x] * dp_psum_B[x - 1])
    
    return win_num
    
def solution(_dice):
    global N, max_score, dice
    dice = _dice
    N = len(dice) // 2
    max_score = N * 100
    
    max_wins = -1
    best_comb = []
    for comb_A in combinations(range(N * 2), N):
        comb_B = tuple(num for num in range(N * 2) if num not in comb_A)
        cur_wins = get_A_wins_num(comb_A, comb_B)
        if cur_wins > max_wins:
            max_wins = cur_wins
            best_comb = list(comb_A)
        
    return [bc + 1 for bc in best_comb]