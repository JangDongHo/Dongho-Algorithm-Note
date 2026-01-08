function solution(players, m, k) {
    let result = 0;
    
    // dp[t]: t 시간까지 봤을 때, 증설된 서버의 수
    dp = Array(24).fill(0);
    
    // 시뮬레이션
    for (let t = 0; t < players.length; t++) {
        const current = dp[t];
        const need = Math.floor(players[t] / m);
        const x = need - current;
        
        // 운영 중인 서버 < 필요한 서버
        if (x > 0) {
            for (let i = t; i < Math.min(t + k, players.length); i++) {
                dp[i] += x;
            }
            result += x;
        }
    }
    
    return result;
}