# https://school.programmers.co.kr/learn/courses/30/lessons/258709

from itertools import combinations

def get_idx(lst, value):
    cur = -1
    step = len(lst)
    
    while step != 0:
        while cur + step < len(lst) and (lst[cur + step] < value):
            cur += step
        step //= 2
    
    return cur

def solution(_dice):
    get_idx([1,2,3,4,5], 4)
    
def get_A_wins_num(comb_A, comb_B):
    global N, dice
    
    list_A = [0]
    list_B = [0]
    
    for n in range(1, N + 1):
        nxt_A = []
        for num in list_A:
            for d in dice[comb_A[n - 1]]:
                nxt_A.append(num + d)
        
        nxt_B = []
        for num in list_B:
            for d in dice[comb_B[n - 1]]:
                nxt_B.append(num + d)
        
        list_A = nxt_A
        list_B = nxt_B
    
    list_A = sorted(list_A)
    list_B = sorted(list_B)
    
    win_num = 0
    for score in list_A:
        num = get_idx(list_B, score) + 1
        win_num += num
    
    return win_num
    
def solution(_dice):
    global N, max_score, dice
    dice = _dice
    N = len(dice) // 2
    
    max_wins = -1
    best_comb = []
    for comb_A in combinations(range(N * 2), N):
        comb_B = tuple(num for num in range(N * 2) if num not in comb_A)
        cur_wins = get_A_wins_num(comb_A, comb_B)
        if cur_wins > max_wins:
            max_wins = cur_wins
            best_comb = list(comb_A)
        
    return [bc + 1 for bc in best_comb]