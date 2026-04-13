def solution(mats, park):
    n = len(park)
    m = len(park[0])
    
    # park 변형
    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                park[i][j] = 0
            else:
                park[i][j] = 1
    
    # 2차원 누적합 생성 (1-index)
    # psum[i][j] = (1,1)부터 (i,j)까지의 합
    psum = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + park[i - 1][j - 1]
    
    # 가져온 돗자리 크기 별로 내림차순 순회
    sorted_mats = sorted(mats, reverse=True)
    for mat in sorted_mats:
        for si in range(1, n + 1):
            ei = si + mat - 1
            for sj in range(1, m + 1):
                ej = sj + mat - 1
                if ei <= n and ej <= m:
                    # (si,sj) 부터 (ei,ej)까지 누적합이 0이면 돗자리 깔기 가능
                    can_place = psum[ei][ej] - (psum[ei][sj - 1] + psum[si - 1][ej] - psum[si - 1][sj - 1])
                    if can_place == 0:
                        return mat
    
    return -1
    