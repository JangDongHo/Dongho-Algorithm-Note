N = int(input())
money_list = list(map(int, input().split()))
M = int(input())


# money list 계산 함수
def sum_money_list(limit_money):
  result = 0
  for money in money_list:
    result += min(money, limit_money)
  return result


# 이분 탐색 함수
def binary_search(start, end):
  result = 0  # 최적의 예산 상한선을 저장하기 위한 변수
  while start <= end:
    mid = (start + end) // 2
    total = sum_money_list(mid)
    if total <= M:
      result = mid  # 현재 mid 값을 result에 저장
      start = mid + 1  # 더 큰 값 탐색
    else:
      end = mid - 1  # 더 작은 값 탐색
  return result


start = 0
end = max(money_list)
result = binary_search(start, end)
print(result)
