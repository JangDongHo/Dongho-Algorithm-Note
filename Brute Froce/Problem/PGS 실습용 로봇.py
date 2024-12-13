# https://school.programmers.co.kr/learn/courses/15009/lessons/121687

def solution(command):
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    d_idx = 0
    answer = [0,0]
    
    for c in command:
        if c == 'R':
            d_idx = (d_idx+1)%4
        elif c == 'L':
            d_idx = (d_idx-1)%4
        elif c == 'G':
            answer[0]+=d[d_idx][0]
            answer[1]+=d[d_idx][1]
        else:
            answer[0]-=d[d_idx][0]
            answer[1]-=d[d_idx][1]

    return answer