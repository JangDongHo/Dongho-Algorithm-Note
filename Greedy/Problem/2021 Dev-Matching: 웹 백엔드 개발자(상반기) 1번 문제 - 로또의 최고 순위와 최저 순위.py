# https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=python3

def solution(lottos, win_nums):
    cnt_0 = 0
    cnt_same = 0
    
    for cur_num in lottos:
        if cur_num == 0:
            cnt_0 += 1
        elif cur_num in win_nums:
            cnt_same += 1
    
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    answer = [rank[cnt_same + cnt_0], rank[cnt_same]]
    return answer