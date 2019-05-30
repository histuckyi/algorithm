"""
백준 6359. 만취한 상범
blog : https://daimhada.tistory.com/182
problem : https://www.acmicpc.net/problem/6359
"""

import sys
input = sys.stdin.readline


def solve(dom, k, n):

    if k == n + 1:
        print(dom.count(1))
        return

    # k간격 만큼 문 열고 닫기
    for i in range(k-1, n, k):
        if dom[i] == 0: dom[i] = 1
        elif dom[i] == 1: dom[i] = 0
    solve(dom, k+1, n)


if __name__ == '__main__':
    n = int(input().strip())
    for i in range(n):
        count = int(input().strip()) # 감옥의 총 수
        dom = [0]*count # 감옥
        solve(dom, 1, count)
