// https://www.acmicpc.net/problem/11399

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/input.txt`;
let input = fs.readFileSync(filePath).toString().trim().split('\n');

// 입력 처리
const N = +input[0];
const times = input[1].split(" ").map(Number);

// 오름차순 정렬
times.sort((a, b) => a - b);

let total = 0;
let sum = 0;

for (let i = 0; i < N; i++) {
  sum += times[i];  // 현재 사람까지 기다린 총 시간
  total += sum;     // 전체 합에 추가
}

console.log(total);