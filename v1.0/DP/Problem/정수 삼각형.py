'''
난이도: 1.5
목표 시간: 30분
시간 제한: 2초
메모리 제한: 128MB

1회독 성공 여부: 실패
2회독 성공 여부: 성공
풀이 시간: 16분
'''
'''
접근 방식
- array 변수는 초기 '정수 삼각형' 정보
- dp 변수는 다이나믹 프로그래밍을 위한 2차원 테이블이라고 가정
- 점화식: dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j])
- 단, dp 테이블에 접근해야 할 때마다 리스트의 범위를 벗어나지 않는지 체크할 필요가 있음
- 또한, 구현의 편의상 초기 데이터를 담는 array 변수를 사용하지 않고, 바로 dp 테이블에 초기 데이터를 담아서 점화식에 따라서 dp 테이블을 갱신 할 수 있다.
'''

### 2회독 성공 코드
N = int(input())
dp = []
for _ in range(N):
  dp.append(list(map(int, input().split())))

for i in range(1, N):
  for j in range(len(dp[i])):
    # 배열 맨 왼쪽 요소 계산
    if j == 0:
      dp[i][j] += dp[i - 1][j]
    # 배열 맨 오른쪽 요소 계산
    elif j == len(dp[i]) - 1:
      dp[i][j] += dp[i - 1][j - 1]
    # 그 외 나머지 요소 계산
    else:
      dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[-1]))

### 책 코드
n = int(input())
dp = []
for _ in range(n):
  dp.append(list(map(int, input().split())))

for i in range(1, n):
  for j in range(i + 1):
    # 좌측 위로 이동
    if j == 0:
      up_left = 0
    else:
      up_left = dp[i - 1][j - 1]
    # 우측 위로 이동
    # 우측 위로 이동
    if j == i:
      up_right = 0
    else:
      up_right = dp[i - 1][j]
    dp[i][j] = dp[i][j] + max(up_left, up_right)

print(max(dp[-1]))
