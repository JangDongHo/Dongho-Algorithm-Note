// https://www.acmicpc.net/problem/1927

class MinHeap {
  constructor() {
    this.heap = [];
  }

  getParentIndex(index) {
    return Math.floor((index - 1) / 2);
  }

  getLeftChildIndex(index) {
    return 2 * index + 1;
  }

  getRightChildIndex(index) {
    return 2 * index + 2;
  }

  size() {
    return this.heap.length;
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  heappush(value) {
    this.heap.push(value);
    this.heapifyUp();
  }

  heapifyUp() {
    let index = this.size() - 1;

    while (index > 0 && this.heap[this.getParentIndex(index)] > this.heap[index]) {
      this.swap(index, this.getParentIndex(index));
      index = this.getParentIndex(index);
    }
  }

  heappop() {
    if (this.size() === 0) return 0;
    if (this.size() === 1) return this.heap.pop();

    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();

    return min;
  }

  heapifyDown() {
    let index = 0;

    while (this.getLeftChildIndex(index) < this.size()) {
      let smallerChildIndex = this.getLeftChildIndex(index);
      const rightChildIndex = this.getRightChildIndex(index);

      if (rightChildIndex < this.size() && this.heap[rightChildIndex] < this.heap[smallerChildIndex]) {
        smallerChildIndex = rightChildIndex;
      }

      if (this.heap[index] <= this.heap[smallerChildIndex]) break;

      this.swap(index, smallerChildIndex);
      index = smallerChildIndex;
    }
  }
}

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;
let input = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);

N = input[0];
commands = input.slice(1);
let answer = "";

const heap = new MinHeap();
for (c of commands) {
  if (c === 0) {
    answer += heap.heappop() + "\n";
  } else {
    heap.heappush(c);
  }
}
console.log(answer);
