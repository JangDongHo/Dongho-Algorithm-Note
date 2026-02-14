""" solve.py for 5397번. 키로거 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def build_string(data: list[str], nxt: list[int]) -> str:
    cur = nxt[0]
    out = []
    while cur != -1:
        out.append(data[cur])
        cur = nxt[cur]
    return "".join(out)


def insert(addr: int, val: str, data: list[str], prev: list[int], nxt: list[int], unused: int) -> tuple[int, int]:
    data[unused] = val
    prev[unused] = addr
    nxt[unused] = nxt[addr]

    if nxt[addr] != -1:
        prev[nxt[addr]] = unused
    nxt[addr] = unused

    return unused, unused + 1


def move_left(addr: int, prev: list[int]) -> int:
    return prev[addr] if addr != 0 else addr


def move_right(addr: int, nxt: list[int]) -> int:
    return nxt[addr] if nxt[addr] != -1 else addr


def delete(addr: int, prev: list[int], nxt: list[int]) -> int:
    if addr == 0:
        return 0

    nxt[prev[addr]] = nxt[addr]
    if nxt[addr] != -1:
        prev[nxt[addr]] = prev[addr]

    return prev[addr]


def solve(log: str):
    MX = len(log) + 1
    data = [''] * MX
    prev = [-1] * MX
    nxt = [-1] * MX

    cursor = 0
    unused = 1

    for ch in log:
        match ch:
            case '-':
                cursor = delete(cursor, prev, nxt)
            case '<':
                cursor = move_left(cursor, prev)
            case '>':
                cursor = move_right(cursor, nxt)
            case _:
                cursor, unused = insert(cursor, ch, data, prev, nxt, unused)

    return build_string(data, nxt)


def main():
    L = int(sys_input())

    for _ in range(L):
        log = sys_input()
        answer = solve(log)
        print(answer)


if __name__ == "__main__":
    main()
