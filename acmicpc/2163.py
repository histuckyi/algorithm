"""
백준 2163. 초콜릿 자르기
blog : https://daimhada.tistory.com/180
problem : https://www.acmicpc.net/problem/2163
"""

import sys
input = sys.stdin.readline

def solve(n, m):
    return (n-1) + n * (m-1)


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    print(solve(n, m))