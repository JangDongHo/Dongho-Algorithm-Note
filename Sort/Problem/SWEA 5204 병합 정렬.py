# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

def merge_sort(arr, i):
    global cnt

    # Base Case
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid], i + 1)
    high_arr = merge_sort(arr[mid:], i + 1)

    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 cnt + 1
    if low_arr[-1] > high_arr[-1]:
        cnt += 1

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    cnt = 0
    x = merge_sort(num_list, 0)[N // 2]

    print(f"#{tc} {x} {cnt}")
