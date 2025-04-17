const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/input.txt`;
let input = fs.readFileSync(filePath).toString().trim().split('\n');

// 입력 값 받기
N = +input[0];
shirts = input[1].split(' ').map(Number);
[T, P] = input[2].split(' ').map(Number);

t_cnt = p_cnt = 0
for (let shirt of shirts) {
  t_cnt += Math.ceil(shirt / T);
}

console.log(t_cnt);
console.log(Math.floor(N / P), N % P);

