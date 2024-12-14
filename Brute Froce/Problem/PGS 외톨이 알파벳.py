# https://school.programmers.co.kr/learn/courses/15008/lessons/121683

def solution(input_string):
    seen = set()
    ans = set()
    
    prev_c = input_string[0]
    seen.add(prev_c)
    
    for i in range(1, len(input_string)):
        c = input_string[i]
        if c != prev_c and c in seen:
            ans.add(c)
        seen.add(c)
        prev_c = c
    
    return "".join(sorted(ans)) if ans else "N"