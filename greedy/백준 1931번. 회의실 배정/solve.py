N = int(input())
rooms = [tuple(map(int, input().split())) for _ in range(N)]

rooms.sort(key=lambda x: (x[1], x[0]))

last_room = rooms[0]
answer = 1

for i in range(1, N):
	cur_room = rooms[i]

	if last_room[1] <= cur_room[0]:
		last_room = cur_room
		answer += 1

print(answer)