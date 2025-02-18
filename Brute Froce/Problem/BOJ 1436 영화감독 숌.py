def find_end_number(N):
    count = 0
    num = 666

    while True:
        if '666' in str(num):
            count += 1
            if count == N:
                return num
        num += 1

# 입력값 받기
N = int(input())
print(find_end_number(N))