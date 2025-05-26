const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/input.txt`;
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const M = +input[0];
const S = new Set();
const output = [];

for (let i = 1; i <= M; i++) {
  const [command, val] = input[i].split(' ');
  const num = +val;
  
  switch(command) {
    case 'add':
      S.add(num);
      break;
    case 'remove':
      S.delete(num);
      break;
    case 'check':
      output.push(S.has(num) ? 1 : 0);
      break;
    case 'toggle':
      if (S.has(num)) S.delete(num);
      else S.add(num);
      break;
    case 'all':
      S.clear();
      for (let j = 1; j <= 20; j++) {
        S.add(j)
      }
      break;
    case 'empty':
      S.clear();
      break;
  }
}

console.log(output.join('\n'));