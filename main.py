def mod(a, b, m):
    # Base Case
    if b == 1:
        return a % m

    # Recursive Case
    ret = mod(a, b//2, m)
    ret = (ret * ret) % m
    if b % 2 != 0:  # b가 홀수일 경우 추가적으로 a를 곱함
        ret = (ret * a) % m
    return ret

A, B, C = map(int, input().split())
print(mod(A, B, C))