'''
난이도: 1.5
목표 시간: 40분
시간 제한: 1초
메모리 제한: 256MB

성공 여부: 실패
'''
'''
접근 방식
- 이 문제의 기본 아이디어는 '가장 긴 증가하는 부분 수열(LIS)'로 알려진 전형적인 다이나믹 프로그래밍 문제의 아이디어와 같다.
- LIS 문제란, 하나의 수열이 주어졌을 때 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제이다.
- 'D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이'라고 정의하면, 가장 긴 증가한 부분 수열을 계산하는 점화식은 다음과 같다.
  - 이때 초기의 DP 테이블의 값은 모두 1로 초기화한다.
  - 모든 0 <= j < i에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
'''

### 책 코드
N = int(input())
input_list = list(map(int, input().split()))
input_list.reverse()
dp = [1] * N

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘
for i in range(1, N):
  for j in range(i):
    if input_list[j] < input_list[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
