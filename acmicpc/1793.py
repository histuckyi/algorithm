"""
백준 1793. 타일링
blog : https://daimhada.tistory.com/178
problem : https://www.acmicpc.net/problem/1793
"""

import sys
input = sys.stdin.readline

def dp(start, n, memo):

    # 마지막 위치까지 타일링 완료
    if start == n:
        return 1

    # 범위를 초과한 타일 처리
    if n < start:
        return 0

    # 저장된 값 활용하기
    if (start, n) in memo:
        return memo[(start, n)]

    # memoization
    memo[(start, n)] = dp(start + 1, n, memo) + 2*dp(start+2, n, memo)
    return memo[(start, n)]


if __name__ == "__main__":
    memo = {}
    try:
        while True:
            n = int(input().strip())
            print(dp(0, n, memo))
    except:
        pass