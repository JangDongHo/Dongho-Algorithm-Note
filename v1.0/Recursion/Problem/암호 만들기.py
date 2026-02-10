### 풀이1. 내가 처음 제출한 코드 (직접 구현)
# 모음 개수 세는 함수
def count_vowel(password):
	cnt = 0
	vowels = ['a', 'e', 'i', 'o', 'u'] # 모음
	for vowel in vowels:
		if vowel in password:
			cnt += 1
	return cnt

# 조합 재귀함수
def combination(index, level):
	global L, C, I, password, vowels
	if level == L:
		cnt_vowel = count_vowel(password)
		# 최소 한 개의 모음, 두 개의 자음으로 구성돼있는 패스워드만 출력
		if cnt_vowel >= 1 and L - cnt_vowel >= 2:
			for u in password:
				print(u, end='')
			print()
		return

	for i in range(index, C):
		password.append(I[i])
		combination(i+1, level+1)
		password.pop()


L, C = map(int, input().split()) # 3 <= L <= C <= 15
I = sorted(list(input().split())) # C개의 정렬된 문자 리스트
password = []
combination(0, 0)


### 풀이2. 직접 구현 다른 풀이
vows = ['a', 'e', 'i', 'o', 'u']
choose = []


def is_possible():
	global L, C, choose, arr

	vow = 0
	for c in choose:
		vow += (c in vows)
	con = L - vow

	return (vow >= 1 and con >= 2)

def combination(idx, lev):
	global L, C, choose, arr

	# base case
	if lev == L:
		if is_possible():
			print(''.join(choose))
		return

	# recursive case
	for i in range(idx, C):
		choose.append(arr[i])
		combination(i + 1, lev + 1)
		choose.pop()


L, C = map(int, input().split())
arr = input().split()

arr.sort()

combination(0, 0)

### 풀이3. 라이브러리 이용
from itertools import combinations


vows = ['a', 'e', 'i', 'o', 'u']


def is_possible(word):
	global L, C, arr

	vow = 0
	for w in word:
		vow += (w in vows)
	con = L - vow

	return (vow >= 1 and con >= 2)


L, C = map(int, input().split())
arr = input().split()

arr.sort()

for word in combinations(arr, L):
	if is_possible(word):
		print(''.join(word))
