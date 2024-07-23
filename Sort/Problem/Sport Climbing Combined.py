n = int(input())
players = [tuple(map(int, input().split())) for _ in range(n)]

sorted_players = sorted(players, key=lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))
for i in range(3):
	print(sorted_players[i][0], end=' ')