# https://www.acmicpc.net/problem/1058

# 입력 값 받기
N = int(input())
friends = [list(input()) for _ in range(N)]

answer = 0
for i in range(N):
    two_friends = set()
    for j in range(N):
        if friends[i][j] == 'Y': # i와 j가 직접 친구일 때
            two_friends.add(j)
            for k in range(N):
                if friends[j][k] == 'Y' and k != i: # 친구의 친구도 찾기
                    two_friends.add(k)
    answer = max(answer, len(two_friends))

print(answer)