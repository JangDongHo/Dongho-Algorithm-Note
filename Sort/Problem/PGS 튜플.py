# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    tmp_s = s.lstrip('{').rstrip('}').split('},{')
    
    tuples = []
    for ts in tmp_s:
        tuples.append(ts.split(','))
    
    tuples.sort(key = len)    
    
    for tup in tuples:
        for n in tup:
            if int(n) not in answer:
                answer.append(int(n))
    
    return answer