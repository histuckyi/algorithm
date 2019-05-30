"""
백준 2309. 일곱 난쟁이
blog : https://daimhada.tistory.com/163
problem : https://www.acmicpc.net/problem/2309
"""

import sys
from itertools import combinations
input = sys.stdin.readline

def solve(case):
    if sum(case) == 100:
        case = list(case)
        case.sort()
        for old in case:
            print(int(old))
        return True
    return False

if __name__ == "__main__":
    child = set()
    for i in range(9):
        nai = int(input().strip())
        if nai <= 100:
            child.add(nai)

    for case in combinations(child, 7):
        if solve(case):
            break
