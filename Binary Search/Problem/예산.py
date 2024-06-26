'''
난이도: 실버2
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
접근 방법
이 문제를 해결하기 위해 이분 탐색(Binary Search)을 사용한다. 이분 탐색을 통해 가능한 예산 상한선의 범위를 좁혀가며 최적의 상한선을 찾아낸다.

필요한 함수는 다음과 같다.
1. 합계 계산 함수: 주어진 상한선에 따라 실제 배정될 예산의 합계를 계산하는 함수 sum_money_list를 정의한다.
2. 이분 탐색 함수: 주어진 범위 내에서 가능한 최대 예산 상한선을 찾기 위한 이분 탐색 함수 binary_search를 정의한다.
'''


def sum_money_list(limit_money, money_list):
  result = 0
  for money in money_list:
    result += min(money, limit_money)
  return result


def binary_search(start, end, money_list, M):
  result = 0  # 최적의 예산 상한선을 저장하기 위한 변수
  while start <= end:
    mid = (start + end) // 2
    total = sum_money_list(mid, money_list)
    if total <= M:
      result = mid  # 현재 mid 값을 result에 저장
      start = mid + 1  # 더 큰 값 탐색
    else:
      end = mid - 1  # 더 작은 값 탐색
  return result


N = int(input())
money_list = list(map(int, input().split()))
M = int(input())

start = 0
end = max(money_list)
result = binary_search(start, end, money_list, M)
print(result)
