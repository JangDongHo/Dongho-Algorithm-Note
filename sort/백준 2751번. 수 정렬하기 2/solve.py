"""백준 2751번 수 정렬하기 2"""

import sys
input = sys.stdin.readline

def merge_sort(st: int, en: int) -> None:
    if st + 1 == en:
        return

    mid = (st + en) // 2
    merge_sort(st, mid)
    merge_sort(mid, en)
    merge(st, en)


def merge(st: int, en: int) -> None:
    mid = (st + en) // 2
    left = st
    right = mid
    idx = st

    while left < mid and right < en:
        if arr[left] < arr[right]:
            tmp[idx] = arr[left]
            left += 1
        else:
            tmp[idx] = arr[right]
            right += 1
        idx += 1

    while left < mid:
        tmp[idx] = arr[left]
        left += 1
        idx += 1

    while right < en:
        tmp[idx] = arr[right]
        right += 1
        idx += 1

    for i in range(st, en):
        arr[i] = tmp[i]

N = int(input())
arr = [int(input()) for _ in range(N)]
tmp = [0] * N

merge_sort(0, N)
print(*arr, sep="\n")