'''
난이도: 1.5
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 성공
풀이 시간: 50분
'''
'''
접근 방식
- 2차원 테이블을 이용한 다이나믹 프로그래밍으로 해결할 수 있다.
- 금광의 모든 위치에 대하여 오른쪽 위로 가는 경우, 오른쪽으로 가는 경우, 오른쪽 아래로 가는 경우 중에서 가장 많은 금을 가지고 있는 경우를 테이블에 저장해주어 문제를 해결하였다.
'''
### 내가 푼 코드

T = int(input())

# 방향 정의(오른쪽 위, 오른쪽, 오른쪽 아래)
steps = [(1, -1), (1, 0), (1, 1)]


def find_max_root(cave_map, m, n):
  result_map = [[0] * m for i in range(n)]
  for y in range(n):
    result_map[y][0] = cave_map[y][0]
  for x in range(m - 1):
    for y in range(n):
      for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        if 0 <= nx < m and 0 <= ny < n:
          result_map[ny][nx] = max(cave_map[ny][nx] + result_map[y][x],
                                   result_map[ny][nx])
  for y in range(n):
    result = 0
    result = max(result, result_map[y][-1])
  return result


for _ in range(T):
  n, m = map(int, input().split())
  data = list(map(int, input().split()))
  cave_map = [[0] * m for i in range(n)]
  for i in range(n):
    for j in range(m):
      cave_map[i][j] = data[m * i + j]
  print(find_max_root(cave_map, m, n))
'''
접근 방식
- dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
'''
### 책 코드
# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
  # 금광 정보 입력
  n, m = map(int, input().split())
  array = list(map(int, input().split()))

  # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
  dp = []
  index = 0
  for i in range(n):
    dp.append(array[index:index + m])
    index += m

  # 다이나믹 프로그래밍 진행
  for j in range(1, m):
    for i in range(n):
      # 왼쪽 위에서 오는 경우
      if i == 0:
        left_up = 0
      else:
        left_up = dp[i - 1][j - 1]
      # 왼쪽 아래에서 오는 경우
      if i == n - 1:
        left_down = 0
      else:
        left_down = dp[i + 1][j - 1]
      # 왼쪽에서 오는 경우
      left = dp[i][j - 1]
      dp[i][j] = dp[i][j] + max(left_up, left_down, left)

  result = 0
  for i in range(n):
    result = max(result, dp[i][m - 1])

  print(result)
