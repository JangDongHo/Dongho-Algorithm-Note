function solution(info, n, m) {
    const N = info.length;
    const INF = 1e9;
    
    // 1. DP 생성
    const dp = Array.from({ length: N + 1 }, () => Array(m).fill(INF));
    
    // 2. DP 초기화
    dp[0][0] = 0;
    
    // 3. 점화식
    for (let i = 0; i < N; i++) {
        const [aCost, bCost] = info[i];
        
        for (let b = 0; b < m; b++) {
            if (dp[i][b] === INF) continue;
            
            // A 도둑이 i번 물건을 훔치는 경우
            if (dp[i][b] + aCost < n) {
                dp[i + 1][b] = Math.min(dp[i + 1][b], dp[i][b] + aCost)
            }
            
            // B 도둑이 i번 물건을 훔치는 경우
            if (b + bCost < m) {
                dp[i + 1][b + bCost] = Math.min(dp[i + 1][b + bCost], dp[i][b])   
            }
        }
    }
    
    // 4. 최종 답
    const answer = Math.min(...dp[N]);
    return answer === INF ? -1 : answer;
}