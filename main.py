def merge_sort(arr):
    # Base Case: 배열 길이가 1 이하이면 정렬할 필요 없음
    if len(arr) <= 1:
        return arr
    
    # Recursive Case: 배열을 반으로 나누어 정렬
    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    # 두 정렬된 배열을 병합하여 반환
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    i, j = 0, 0

    # 두 배열을 정렬하면서 합치기
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # 남아 있는 요소들 추가
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

N, K = map(int, input().split())
arr = list(map(int, input().split()))
sorted_arr = merge_sort(arr)
print(sorted_arr)