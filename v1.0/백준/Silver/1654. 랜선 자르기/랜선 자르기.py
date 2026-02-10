# 자를 길이(h)로 랜선들을 잘랐을 때 나오는 랜선 개수
def count_line(lines, h):
    count = 0
    for line in lines:
        count += line // h
    return count

# 자를 길이(h)를 파라매트릭 서치로 결정
def parametric_search(lines, target):
    max_h = 0

    left = 1
    right = max(lines)

    while(left <= right):
        mid = (left + right) // 2
        if count_line(lines, mid) >= target:
            left = mid + 1
            max_h = mid
        else:
            right = mid - 1

    return max_h

# 메인 함수
def main():
    K, N = map(int, input().split())
    lines = [int(input()) for _ in range(K)]
    result = parametric_search(lines, N)
    print(result)

main()