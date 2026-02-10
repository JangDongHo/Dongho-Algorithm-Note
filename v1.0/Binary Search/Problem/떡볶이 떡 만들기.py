'''
난이도: 2
목표 시간: 40분
시간 제한: 2초
메모리 제한: 128MB

성공 여부: 실패
'''
'''
시간 복잡도 분석
- 최악의 경우 높이가 최대 10억일 때, 이진 탐색으로 찾는다면 대략 31번 만에 경우의 수를 모두 고려할 수 있다.
- 이때 떡의 개수 N이 최대 100만 개이므로 이진 탐색으로 절단기의 높이 H를 바꾸면서, 바꿀 때마다 모든 떡을 체크하는 경우 대략 최대 3,000만 번 정도의 연산으로 문제를 풀 수 있다.
'''

# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while (start <= end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    # 잘랐을 때의 떡볶이 양 계산
    if x > mid:
      total += x - mid
  # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
  if total < m:
    end = mid - 1
  # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
  else:
    result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
    start = mid + 1

# 정답 출력
print(result)
