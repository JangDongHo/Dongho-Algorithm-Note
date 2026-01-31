const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/input.txt`;
const input = fs.readFileSync(filePath).toString();

const N = Number(input);
const MOD = 10_007;

// dp[n][i] : n번째 자리에 i가 들어왔을 때 가능한 경우의 수
const dp = Array.from({ length: N + 1 }, () => Array(10).fill(0));

// DP 초기화
dp[1].fill(1);

// DP
for (let n = 2; n <= N; n++) {
  for (let i = 0; i <= 9; i++) {
    let sum = 0;
    for (let j = i; j <= 9; j++) {
      sum = (sum + dp[n - 1][j]) % MOD;
    }
    dp[n][i] += sum;
  }
}

// 결과
let answer = 0;
for (let i = 0; i <= 9; i++) {
  answer = (answer + dp[N][i]) % MOD;
}

console.log(answer);