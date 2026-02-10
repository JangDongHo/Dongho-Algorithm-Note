import sys
from collections import Counter

trees = defaultdict(int)
all_cnt = 0

while True:
	tree = sys.stdin.readline().rstrip()
	if not tree:
		break
	all_cnt += 1
	trees[tree] += 1

# 백분율 계산
for key, value in sorted(trees.items()):
	ratio = value / all_cnt * 100
	print("%s %.4f" % (key, ratio))
