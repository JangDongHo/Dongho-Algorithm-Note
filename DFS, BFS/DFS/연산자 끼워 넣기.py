'''
난이도: 2
목표 시간: 30분
시간 제한: 2초
메모리 제한: 512MB

성공 여부: 실패
'''
'''
접근 방법
- 재귀적으로 푸는 문제라는 것을 이해하는 것까지는 성공
- 하지만, 구현 부분에서 실패했다. DFS에 대한 이해가 아직 부족한 것 같다.
'''


### 내가 푼 코드 (실패)
def calculate_number(prev_num, index):
  if index >= len(number_list):
    return
  if sum(sign_list) == 0:
    result.append(prev_num)
    return
  now_num = number_list[index]
  if sign_list[0] > 0:
    sign_list[0] -= 1
    calculate_number(prev_num + now_num, index + 1)
  if sign_list[1] > 0:
    sign_list[1] -= 1
    calculate_number(prev_num - now_num, index + 1)
  if sign_list[2] > 0:
    sign_list[2] -= 1
    calculate_number(prev_num * now_num, index + 1)
  if sign_list[3] > 0:
    sign_list[3] -= 1
    calculate_number(prev_num // now_num, index + 1)


n = int(input())
number_list = list(map(int, input().split()))
sign_list = list(map(int, input().split()))
result = []
calculate_number(number_list[0], 1)
print(min(result))
print(max(result))

### 책 코드
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9


# 깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
  global min_value, max_value, add, sub, mul, div
  # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
  if i == n:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    # 각 연산자에 대하여 재귀적으로 수행
    if add > 0:
      add -= 1
      dfs(i + 1, now + data[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i + 1, now - data[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i + 1, now * data[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i + 1, int(now / data[i]))  # 나눌 때는 나머지를 제거
      div += 1


# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)
