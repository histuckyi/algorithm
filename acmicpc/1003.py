"""
백준 1003. 피보나치 함수
blog : https://daimhada.tistory.com/90
problem : https://www.acmicpc.net/problem/1003
"""

import sys
input = sys.stdin.readline

def solve(n):
    global fibolist
    return fibolist[n]


if __name__ == "__main__":
    fibolist = [(1, 0), (0, 1)]
    for i in range(2, 41):
        first = fibolist[i-2][0] + fibolist[i-1][0]
        second = fibolist[i-2][1] + fibolist[i-1][1]
        fibolist.append((first, second))

    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        result = solve(n)
        print("{0} {1}".format(result[0], result[1]))
