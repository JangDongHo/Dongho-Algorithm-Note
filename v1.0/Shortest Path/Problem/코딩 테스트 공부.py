# https://school.programmers.co.kr/learn/courses/30/lessons/118668

from queue import PriorityQueue

INF = int(1e9)

def solution(alp, cop, problems):
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    
    target_alp = max([problem[0] for problem in problems] + [alp])
    target_cop = max([problem[1] for problem in problems] + [cop])
    
    times = [[INF for _ in range(target_cop + 1)] for _ in range(target_alp + 1)]
    
    # Sovle (다익스트라)
    pq = PriorityQueue()
    pq.put((0, alp, cop)) # (소요 시간, 알고력, 코딩력)
    times[alp][cop] = 0
    
    while not pq.empty():
        cur_time, cur_alp, cur_cop = pq.get()
        
        if (cur_alp >= target_alp) and (cur_cop >= target_cop):
            return cur_time
        
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            nxt_time = cur_time + cost
            nxt_alp = min(target_alp, cur_alp + alp_rwd)
            nxt_cop = min(target_cop, cur_cop + cop_rwd)
            if (cur_alp >= alp_req) and (cur_cop >= cop_req) and (nxt_time < times[nxt_alp][nxt_cop]):
                pq.put((nxt_time, nxt_alp, nxt_cop))
                times[nxt_alp][nxt_cop] = nxt_time
    
    