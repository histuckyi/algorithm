"""
백준 1563. 개근상
blog :
problem : https://www.acmicpc.net/problem/1563
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
memo = {} # memoization

def dp(total, day, late, abs):

    # 지각이 2번 이상이면 fail
    if 2 <= late:
        return 0

    # 결석 3연속이면 fail
    if 3 <= abs:
        return 0

    # 개근상 조건 충족
    if day == total:
        return 1

    # memoization 기록 가져오기
    # day, late, abs가 다음과 같은 값일 경우 개근상을 받을 수 있는 경우의 수
    if (day, late, abs) in memo:
        return memo[(day, late, abs)]

    # day째 되는 날에, 그 이후 날들에 출석하거나 지각하거나,결석하였을 때 개근상을 받을 수 있는 경우의 수에 대한 기록
    memo[(day, late, abs)] = dp(total, day + 1, late, 0) + dp(total, day +1, late +1, 0) + dp(total, day +1, late, abs + 1)
    return memo[(day, late, abs)]


if __name__ == "__main__":
    total = int(input().strip())
    # 출석 일 수, 지각수, 연속 결석 수
    print(dp(total, 0, 0, 0) % 1000000)

