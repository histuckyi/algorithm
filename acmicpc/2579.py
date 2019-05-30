"""
백준 2579. 계단 오르기
blog : https://daimhada.tistory.com/181
problem : https://www.acmicpc.net/problem/2579
"""

import sys
input = sys.stdin.readline


def solve(stair, n):
    dp = []
    dp.append(stair[0])
    for i in range(1, 3):
        if i == 1:
            dp.append(max(dp[i-1] + stair[i], stair[i]))
            continue
        dp.append(max(dp[i-2] + stair[i], stair[i-1] + stair[i]))

    for i in range(3, n):
        # i번째 계단으로 올라오기 위해 max(직전 계단을 밟은 경우, 직전 계단을 밟지 않은 경우)
        dp.append(max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2]))
    # print(dp)
    print(dp[-1])


if __name__ == "__main__":
    stair = []
    n = int(input().strip())
    for i in range(n):
        stair.append(int(input().strip()))

    solve(stair, n)