# https://school.programmers.co.kr/learn/courses/30/lessons/118666

types = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']

def solution(survey, choices):
    score = {t: 0 for t in types} # score[t]: 성격 유형 t의 점수
    
    for s, c in zip(survey, choices):
        if c <= 3:
            score[s[0]] += (4 - c)
        elif c >= 5:
            score[s[1]] += (c - 4)
    
    ans = ""
    for i in range(4):
        s1, s2 = score[types[2 * i]], score[types[2 * i + 1]]
        if s1 >= s2: 
            ans += types[2 * i]
        else: 
            ans += types[2 * i + 1]
    
    return ans