# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD

## 접근1. 브루트 포스 - O(1)

from collections import deque

T = 10
for _ in range(T):
	tc = int(input())
	q = deque(list(map(int, input().split())))
	
	cnt = 1
	while q[-1] > 0:
		if cnt >= 6:
			cnt = 1
		left = q.popleft()
		q.append(left - cnt)
		cnt += 1
	if q[-1] < 0:
		q[-1] = 0

	ans = " ".join(map(str, q))
	print(f"#{tc} {ans}")

## 접근2. 접근1 시간 복잡도 개선 - O(1)

T = 10
for _ in range(T):
    tc = int(input())
    numbers = list(map(int, input().split()))

    # 최솟값이 15보다 크면 각 숫자에서 15의 배수만큼 미리 감소시킴
    if min(numbers) > 15:
        div = min(numbers) // 15 - 1
        for idx in range(len(numbers)):
            numbers[idx] -= 15 * div

    cnt = 1
    while True:
        # 첫 번째 숫자가 0보다 크면 감소시키고 맨 뒤로 보냄
        if numbers[0] > 0:
            tmp = numbers.pop(0)
            numbers.append(tmp - cnt)

        # 마지막 숫자가 0 이하가 되면 종료
        if numbers[len(numbers) - 1] <= 0:
            numbers[len(numbers) - 1] = 0
            break

        cnt += 1
        if cnt == 6:
            cnt = 1

    # 출력 형식에 맞춰 출력
    print('#{} '.format(tc), end='')
    print(*numbers)