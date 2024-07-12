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