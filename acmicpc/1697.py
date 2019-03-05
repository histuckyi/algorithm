import sys
from collections import deque
input = sys.stdin.readline


def solve():
    while q:
        cur = q.popleft()
        if cur == k:
            return visit[cur]
        nextPos(cur - 1, cur)
        nextPos(cur + 1, cur)
        nextPos(cur * 2, cur)


def nextPos(nex, cur):
    # check range
    # first visit or visit with minimum time
    if maxSize > nex >= 0 and (0 == visit[nex] or visit[cur] + 1 < visit[nex]):
        visit[nex] = visit[cur] + 1
        q.append(nex)

if __name__ == "__main__":
    n, k = map(int, input().split())
    maxSize = 100001
    visit = [0] * maxSize
    q = deque([n])
    print(solve())