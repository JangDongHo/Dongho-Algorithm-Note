n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()


def binary_search(array, target, start, end):
  height = end
  while start <= end:
    height = (start + end) // 2
    sum = 0
    # 설정한 height부터 end까지의 길이 더하기
    
    # 만약 다 더한 길이가 손님이 원하는 길이일 경우
    if sum == target:
      return height
    # 손님이 원하는 길이에 못 미칠 경우
    elif sum < target:
      end = height - 1
    else:
      start = height + 1
  return height


binary_search(n_list, m, 0, n_list[n - 1])
