# https://www.acmicpc.net/problem/2042

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

tree = [0] * (4 * N)

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    left_value = init(2 * node, start, mid)
    right_value = init(2 * node + 1, mid + 1, end)
    tree[node] = left_value + right_value
    return tree[node]

init(1, 0, N - 1)

def find_tree(node, start, end, left, right):
    # 1. 구하고 싶은 구간(left~right)가 현재 트리 구간(start~end)에 포함되지 않는 경우 (범위를 완전히 벗어났을 때)
    if right < start or end < left:
        return 0

    # 2. 구하고 싶은 구간(left~right) 안에 현재 트리 구간(start~end)이 포함되는 경우 (범위안에 완전히 들어왔을 때)
    if left <= start and end <= right:
        return tree[node]
    
    # 3. 그 외의 경우
    mid = (start + end) // 2
    left_value = find_tree(node * 2, start, mid, left, right)
    right_value = find_tree(node * 2 + 1, mid + 1, end, left, right)
    return left_value + right_value

def update_tree(node, start, end, idx, diff):
    # 범위를 완전히 벗어나는 경우
    if idx < start or end < idx:
        return

    tree[node] += diff

    if start != end:
        mid = (start + end) // 2
        update_tree(node * 2, start, mid, idx, diff)
        update_tree(node * 2 + 1, mid + 1, end, idx, diff)

for i in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b - 1]
        arr[b - 1] = c
        update_tree(1, 0, N - 1, b - 1, diff)
    if a == 2:
        print(find_tree(1, 0, N - 1, b - 1, c - 1))