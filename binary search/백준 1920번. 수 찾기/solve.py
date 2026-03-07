"""백준 1920번. 수 찾기"""

import sys

input = sys.stdin.readline


def binary_search(arr: list[int], x: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return 0


def main():
    _ = int(input())
    arr = sorted(map(int, input().split()))

    _ = int(input())
    finds = map(int, input().split())

    result = [binary_search(arr, x) for x in finds]
    print(*result, sep="\n")


if __name__ == "__main__":
    main()
