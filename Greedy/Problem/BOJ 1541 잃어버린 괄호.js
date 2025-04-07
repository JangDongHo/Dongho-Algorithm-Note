const fs = require('fs');

const filePath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/input.txt`;
let input = fs.readFileSync(filePath).toString().trim();

// 1. '-' 기준으로 먼저 나누기
const parts = input.split('-');

// 2. 첫 번째 부분은 그냥 +로 나눠서 모두 더함.
let result = parts[0].split('+').map(Number).reduce((a, b) => a + b, 0);

// 3. 이후 부분은 각각 +로 더한 후 결과에서 빼줌.
for (let i = 1; i < parts.length; i++) {
	const sum = parts[i].split('+').map(Number).reduce((a, b) => a + b, 0);
	result -= sum;
}

console.log(result);