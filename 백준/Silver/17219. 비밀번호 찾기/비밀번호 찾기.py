import sys
input = sys.stdin.readline

# 입력 값 받기
N, M = map(int, input().split())

# 딕셔너리 생성
passwords = {}

# N개의 사이트 주소와 비밀번호 저장
for _ in range(N):
    site, pw = input().split()
    passwords[site] = pw

# M개의 사이트 주소를 입력받고 비밀번호 출력
for _ in range(M):
    site = input().strip()
    print(passwords[site])