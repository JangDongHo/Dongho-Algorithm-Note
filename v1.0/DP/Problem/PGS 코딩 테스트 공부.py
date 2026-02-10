# https://school.programmers.co.kr/learn/courses/30/lessons/118668

INF = int(1e12)

def solution(alp, cop, problems):
    problems.append([0, 0, 1, 0, 1]) # 알고리즘 공부를 문제 형식으로 치환
    problems.append([0, 0, 0, 1, 1]) # 코딩 공부를 문제 형식으로 치환
    
    target_alp = max([problem[0] for problem in problems] + [alp]) # alp >= target_alp 인 경우도 예외처리 필요
    target_cop = max([problem[1] for problem in problems] + [cop]) # cop >= target_cop 인 경우도 예외처리 필요
    
    # Solve(DP - Bottom Up)
    dp = [[INF for _ in range(target_cop + 1)] for _ in range(target_alp + 1)]
    dp[alp][cop] = 0
    
    for cur_alp in range(alp, target_alp + 1):
        for cur_cop in range(cop, target_cop + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if (cur_alp >= alp_req) and (cur_cop >= cop_req):
                    nxt_alp = min(target_alp, cur_alp + alp_rwd)
                    nxt_cop = min(target_cop, cur_cop + cop_rwd)
                    dp[nxt_alp][nxt_cop] = min(dp[nxt_alp][nxt_cop], dp[cur_alp][cur_cop] + cost)
    
    return dp[target_alp][target_cop]