""" 
Indexed Doubly Linked List

- 0번 인덱스를 더미 데이터로 사용
- insert(addr, val): addr 뒤에 노드 삽입
- delete(addr): addr 노드 삭제 (addr은 노드 주소, 값 아님)
- 시간복잡도: 삽입/삭제 O(1), 순회 O(N)
"""

MX = 1000005
data = [0] * MX
pre  = [-1] * MX
nxt  = [-1] * MX
unused = 1


def insert(addr: int, val: int) -> int:
    global unused
    cur = unused
    unused += 1

    data[cur] = val
    pre[cur] = addr
    nxt[cur] = nxt[addr]

    if nxt[addr] != -1:
        pre[nxt[addr]] = cur
    nxt[addr] = cur
    return cur


def delete(addr: int) -> None:
    if addr == 0:  # don't delete dummy head
        return
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]


def traversal(head: int = 0) -> None:
    cur = nxt[head]
    while cur != -1:
        print(data[cur], end=' ')
        cur = nxt[cur]
    print()

insert(0, 10) # 1번지
insert(1, 20) # 2번지
insert(2, 30) # 3번지
delete(1)
traversal()