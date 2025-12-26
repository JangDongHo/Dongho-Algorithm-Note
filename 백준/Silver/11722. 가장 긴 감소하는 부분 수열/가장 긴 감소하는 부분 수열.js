const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/input.txt`;
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = +input[0];
const sequence = input[1].split(" ").map(Number);
let result = 1;

// 1. 1차원 DP 생성
const dp = new Array(N).fill(1);

// 2. 점화식
for (let i = 0; i < N; i++) {
  for (let j = 0; j < i; j++) {
    if (sequence[j] > sequence[i]) {
      dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }
  result = Math.max(result, dp[i]);
}

console.log(result);