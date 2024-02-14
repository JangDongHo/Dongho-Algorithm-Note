'''
난이도: 2
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
접근 방법
- x가 처음 등장하는 인덱스와 x가 마지막으로 등장하는 인덱스를 각각 계산한 뒤에, 그 인덱스의 차이를 계산하여 문제를 해결할 수 있다.
- 데이터가 존재한다면 가장 첫 번째 위치를 찾는 이진 탐색 함수, 다른 하나는 데이터가 존재한다면 가장 마지막 위치를 찾는 이진 탐색 함수 두 개를 사용한다.
'''

### 내가 푼 코드 (시간초과)
import sys

N, x = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().split()))


def count_element(e, index):
  count = 1
  # 좌측 방향 탐색
  if index > 0:
    index = e - 1
    while num_list[index] == e:
      count += 1
      if index > 0:
        index -= 1
      else:
        break
  # 우측 방향 탐색
  if index < N - 1:
    index = e + 1
    while num_list[index] == e:
      count += 1
      if index < N - 1:
        index += 1
      else:
        break
  return count


def find_element(e, start, end):
  while start <= end:
    mid = (start + end) // 2
    if num_list[mid] == e:
      return mid
    elif num_list[mid] > e:
      end = mid - 1
    else:
      start = mid + 1
  return None


index = find_element(x, 0, N - 1)
if not index:
  print(-1)
else:
  print(count_element(x, index))

### GPT 코드
### 참고 블로그: https://areumdawoon.tistory.com/70
import sys

N, x = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().split()))


def binary_search_left(arr, target):
  left, right = 0, len(arr)
  while left < right:
    mid = (left + right) // 2
    if arr[mid] < target:
      left = mid + 1
    else:
      right = mid
  return left


def binary_search_right(arr, target):
  left, right = 0, len(arr)
  while left < right:
    mid = (left + right) // 2
    if arr[mid] > target:
      right = mid
    else:
      left = mid + 1
  return left


left_index = binary_search_left(num_list, x)
right_index = binary_search_right(num_list, x)

count = right_index - left_index

if count == 0:
  print(-1)
else:
  print(count)
