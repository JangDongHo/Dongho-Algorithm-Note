# https://www.acmicpc.net/problem/1931

# 입력값 처리
N = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(N)]

# 정렬
sorted_schedules = sorted(schedules, key = lambda x : (x[1], x[0]))

# 회의 시간 그리디하게 선택
ans = 0
lt = 0

for st, et in sorted_schedules:
	if st >= lt:
		lt = et
		ans += 1

print(ans)