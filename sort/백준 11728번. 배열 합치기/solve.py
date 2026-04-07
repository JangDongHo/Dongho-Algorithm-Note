"""백준 11728번. 배열 합치기"""

N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = []
left, right = 0, 0

# 두 배열 중 작은 값 반복해서 선택
while left < N and right < M:
    if arr1[left] < arr2[right]:
        result.append(arr1[left])
        left += 1
    else:
        result.append(arr2[right])
        right += 1

result.extend(arr1[left:])
result.extend(arr2[right:])

print(*result)