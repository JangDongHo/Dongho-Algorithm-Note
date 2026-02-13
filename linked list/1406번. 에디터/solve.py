""" solve.py for 1406번. 에디터 """
# 링크드 리스트 풀이 버전

import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

MX = 1_000_000 + 5
data = [''] * MX
prev = [-1] * MX
nxt = [-1] * MX
unused = 1

def print_text(head: int = 0) -> str:
    cur = nxt[head]
    out = []
    while cur != -1:
        out.append(data[cur])
        cur = nxt[cur]
    return "".join(out)

def move_left(addr: int) -> int:
    return prev[addr] if addr != 0 else addr

def move_right(addr: int) -> int:
    return nxt[addr] if nxt[addr] != -1 else addr

def insert(addr: int, char: str) -> int:
    global unused
    cur = unused
    data[cur] = char
    prev[cur] = addr
    nxt[cur] = nxt[addr]

    if nxt[addr] != -1:
        prev[nxt[addr]] = cur
    nxt[addr] = cur

    unused += 1
    return cur

def delete(addr: int) -> None:
    nxt[prev[addr]] = nxt[addr]
    if nxt[addr] != -1:
        prev[nxt[addr]] = prev[addr]

def solve(init: str, m: int) -> str:
    cursor = 0
    for c in init:
        cursor = insert(cursor, c)

    for _ in range(m):
        parts = sys_input().split()
        command = parts[0]

        match command:
            case "L":
                cursor = move_left(cursor)
            case "D":
                cursor = move_right(cursor)
            case "B":
                if cursor != 0:
                    to_del = cursor
                    cursor = prev[cursor]
                    delete(to_del)
            case "P":
                cursor = insert(cursor, parts[1])

    return print_text()

def main() -> None:
    init = sys_input()
    M = int(sys_input())
    print(solve(init, M))

if __name__ == "__main__":
    main()