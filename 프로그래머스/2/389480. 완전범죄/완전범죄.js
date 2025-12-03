function solution(info, n, m) {
    // 1. 2차원 DP 생성
    const dp = Array.from({ length: info.length + 1 }, () => Array(m + 1).fill(Infinity))
    
    // 2. DP 초기화
    dp[0][0] = 0
    
    // 3. DP 점화식
    for (let i = 1; i <= info.length; i++) {
        const [aScore, bScore] = info[i - 1];
        
        for (let b = 0; b <= m; b++) {
            if (dp[i - 1][b] + aScore < n) {
                dp[i][b] = Math.min(dp[i][b], dp[i - 1][b] + aScore)   
            }
            
            if (b + bScore < m) {
                dp[i][b + bScore] = Math.min(dp[i][b], dp[i - 1][b])
            }
        }
    }
    
    // 4. 최종 답 구하기
    let answer = Infinity;
    for (let b = 0; b <= m; b++) {
        answer = Math.min(answer, dp[info.length][b]);
    }
    
    
    return answer === Infinity ? -1 : answer;
    
}