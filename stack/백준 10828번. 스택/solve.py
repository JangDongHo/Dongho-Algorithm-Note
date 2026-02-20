""" 백준 10828 스택 """

import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[int]:
    output = []
    stack = []

    for _ in range(n):
        cmd = sys_input().split()
        op = cmd[0]

        match op:
            case 'push':
                stack.append(cmd[1])
            case 'pop':
                output.append(stack.pop() if stack else -1)
            case 'size':
                output.append(len(stack))
            case 'empty':
                output.append(0 if stack else 1)
            case 'top':
                output.append(stack[-1] if stack else -1)
    
    return output


def main() -> int:
    N = int(sys_input())
    answer = solve(N)
    print(*answer, sep='\n')


if __name__ == "__main__":
    main()