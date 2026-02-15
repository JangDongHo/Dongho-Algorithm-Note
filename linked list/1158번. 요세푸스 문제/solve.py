""" solve.py for 1158번. 요세푸스 문제 """

import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, k: int) -> str:
    arr = [i for i in range(1, n + 1)]
    
    cursor = 0
    answer = []

    for _ in range(n):
        cursor += k - 1
        if cursor >= len(arr):
            cursor = cursor % len(arr)

        num = str(arr.pop(cursor))
        answer.append(num)

    return "<" + ", ".join(answer) + ">"


def main():
    N, K = map(int, sys_input().split())
    answer = solve(N, K)
    print(answer)

if __name__ == "__main__":
    main()