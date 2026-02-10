# 참고: https://areumdawoon.tistory.com/70


# left-most index 반환
def binary_search_left(arr, target):
  left, right = 0, len(arr)
  while left < right:
    mid = (left + right) // 2
    if arr[mid] < target:
      left = mid + 1
    else:
      right = mid
  return left


# right-most index 반환
def binary_search_right(arr, target):
  left, right = 0, len(arr)
  while left < right:
    mid = (left + right) // 2
    if arr[mid] > target:
      right = mid
    else:
      left = mid + 1
  return left
