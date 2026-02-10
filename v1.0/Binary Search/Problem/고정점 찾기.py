'''
난이도: 1.5
목표 시간: 20분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 성공
풀이 시간: 13분
'''
'''
접근 방법
- 보통 이진 탐색을 할 때 target이 있는데, 이 문제는 target이 '중간점(mid)'와 동일한다고 가정하고 탐색을 수행하면 된다.
'''

### 내가 푼 코드
N = int(input())
num_list = list(map(int, input().split()))


def binary_search(num_list, start, end):
  while start <= end:
    mid = (start + end) // 2
    if num_list[mid] == mid:
      return mid
    elif num_list[mid] < mid:
      start = mid + 1
    else:
      end = mid - 1
  return -1


print(binary_search(num_list, 0, N - 1))
