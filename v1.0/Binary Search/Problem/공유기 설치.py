'''
난이도: 2
목표 시간: 50분
시간 제한: 2초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
접근 방법
- 이진 탐색으로 '가장 인접한 두 공유기 사이의 거리'를 조절해가며, 매 순간 실제로 공유기를 설치하여 C보다 많은 개수로 공유기를 설치할 수 있는 체크하여 문제를 해결할 수 있다.
- 다만 '가장 인접한 두 공유기 사이의 거리'의 최댓값을 찾아야 하므로, C보다 많은 개수로 공유기를 설치할 수 있다면 '가장 인접한 두 공유기 사이의 거리'의 값을 증가시켜서, 더 큰 값에 대해서도 성립하는지 체크하기 위해 다시 탐색을 수행한다.
'''

### 책 코드
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

### 개선

import sys
input = lambda: sys.stdin.readline().rstrip()

def is_possible(d):
  global arr, N, C

  cnt = 1
  prev_x = arr[0]
  for i in range(1, N):
    cur_x = arr[i]
    if cur_x - prev_x >= d:
      cnt += 1
      prev_x = arr[i]
  
  return (cnt >= C)

def parametric_search():
  cur = -1
  step = int(1e9) + 1

  while step != 0:
    while (cur + step <= int(1e9)) and is_possible(cur + step):
      cur += step
    step //= 2

  return cur


# Input
N, C = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

# Solve
max_dis = parametric_search()
print(max_dis)
