const fs = require('fs');

function isPossible(length, cables, n) {
	let sum = 0;
	cables.forEach((e) => {
		sum += Math.floor(e / length)
	})
	return sum >= n;
}

function binarySearch(left, right, cables, n) {
	let answer = 0;
	while(left <= right) {
		const mid = Math.floor((left + right) / 2);

		if (isPossible(mid, cables, n)) {
			answer = mid;
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return answer;
}

const filePath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/input.txt`;
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [K, N] = input[0].split(' ').map(Number);
const cables = input.slice(1).map(Number);

const answer = binarySearch(1, Math.max(...cables), cables, N)
console.log(answer)