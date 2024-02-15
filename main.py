N, C = map(int, input().split())
house_list = []
for _ in range(N):
  house_list.append(int(input()))
house_list.sort()


def binary_search(house_list, start, end):
  result = 0
  while start <= end:
    mid = (start + end) // 2
    # 앞에서부터 차근차근 설치
    value = house_list[0]
    count = 1
    for i in range(1, N):
      if house_list[i] >= value + mid:
        value = house_list[i]
        count += 1
    if count >= C:
      start = mid + 1
      result = mid
    else:
      end = mid - 1
  return result


print(binary_search(house_list, 1, house_list[N - 1] - house_list[0]))
