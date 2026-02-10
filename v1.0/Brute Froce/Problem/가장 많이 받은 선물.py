# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    N = len(friends)
    I = {name: index for index, name in enumerate(friends)}
    
    gift_matrix = [[0 for _ in range(N)] for _ in range(N)]
    gift_score = [0] * N
    
    # 주고 받은 기록 갱신
    for gift in gifts:
        a, b = gift.split()
        gift_matrix[I[a]][I[b]] += 1
        gift_score[I[a]] += 1
        gift_score[I[b]] -= 1
    
    answers = [0] * N
    for a in range(N):
        for b in range(N):
            if a == b:
                continue
            # Case 1. 이번 달에 a가 b에게 선물을 더 많이 줬다면
            case1 = (gift_matrix[a][b] > gift_matrix[b][a])
            
            # Case 2. a와 b의 선물 주고 받은 개수가 같고, 선물 지수가 a가 더 높다면
            case2 = (gift_matrix[a][b] == gift_matrix[b][a] and gift_score[a] > gift_score[b])
            
            answers[a] += (case1 or case2)
    
    return max(answers)