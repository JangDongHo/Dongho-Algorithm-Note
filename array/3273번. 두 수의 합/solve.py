""" solve.py for 3273번. 두 수의 합 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(nums: list[int], x: int) -> int:
    candidate = set()
    count = 0

    for n in nums:
        if n in candidate:
            count += 1
            candidate.remove(n)
        else:
            candidate.add(x - n)

    return count


def main() -> None:
    n = int(sys_input())
    nums = list(map(int, sys_input().split()))
    x = int(sys_input())

    answer = solve(nums, x)

    print(answer)


if __name__ == "__main__":
    main()