# Input
row_list = []
col_list = [[0 for _ in range(9)] for _ in range(9)]
box_list = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
    row_list.append(list(map(int, input().split())))

for j in range(9):
    for i in range(9):
        col_list[i][j] = row_list[j][i]

print(col_list)