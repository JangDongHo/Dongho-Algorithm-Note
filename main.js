class MinHeap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  heappush(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  heappop() {
    if (this.size() <= 1) return this.heap.pop();

    const root = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return root;
  }

  bubbleUp() {
    let idx = this.size() - 1;
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this.heap[idx] >= this.heap[parentIdx]) break;

      this.swap(idx, parentIdx);
      idx = parentIdx;
    }
  }

  bubbleDown() {
    let idx = 0;
    const length = this.size();
    while (true) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let smallest = idx;

      if (leftIdx < length && this.heap[leftIdx] < this.heap[smallest]) {
        smallest = leftIdx;
      }
      if (rightIdx < length && this.heap[rightIdx] < this.heap[smallest]) {
        smallest = rightIdx;
      }
      if (smallest === idx) break;

      this.swap(idx, smallest);
      idx = smallest;
    }
  }
}

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/input.txt`;
let input = fs.readFileSync(filePath).toString().trim().split('\n');
N = input[0]
commands = input.slice(1).map(Number);
hq = new MinHeap();

for(let c of commands) {
	if (c == 0) {
		const min = hq.heappop();
		console.log(min ? min : 0)
	} else {
		hq.heappush(c);
	}
}
