# https://www.acmicpc.net/problem/24060

import sys
input = sys.stdin.readline

def merge_sort(arr, left, right):
    if left == right:
        return [arr[left]]
    
    mid = (left + right) // 2
    left_sorted = merge_sort(arr, left, mid)
    right_sorted = merge_sort(arr, mid + 1, right)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    global ans
    sorted_arr = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            ans.append(left[i])  # 올바른 값 추가
            i += 1
        else:
            sorted_arr.append(right[j])
            ans.append(right[j])  # 올바른 값 추가
            j += 1

    while i < len(left):
        sorted_arr.append(left[i])
        ans.append(left[i])
        i += 1

    while j < len(right):
        sorted_arr.append(right[j])
        ans.append(right[j])
        j += 1

    return sorted_arr

N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = []

merge_sort(arr, 0, N - 1)

print(ans[K - 1] if len(ans) >= K else -1)
