const fs = require('fs');

const filePath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/input.txt`;
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [K, N] = input[0].split(' ').map(Number);
const cables = input.slice(1).map(Number);

let left = 1;
let right = Math.max(...cables);
let answer = 0;

while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  const count = cables.reduce((sum, len) => sum + Math.floor(len / mid), 0);

  if (count >= N) {
    answer = mid;      // 길이 가능한 경우, 최댓값 갱신
    left = mid + 1;    // 더 길게 잘라도 가능한지 확인
  } else {
    right = mid - 1;   // 너무 많이 잘라서 N개 안 됨 → 길이 줄이기
  }
}

console.log(answer);