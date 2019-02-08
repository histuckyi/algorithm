"""
백준 11047. 동전 0
blog : https://daimhada.tistory.com/43
problem : https://www.acmicpc.net/problem/14889

 pool = ['A', 'B', 'C']
 print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
 print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
"""
import itertools
import sys

def cal(lines, a, b):
    return lines[int(a)][int(b)]

def bruteforce(lines, n):
    count = n // 2
    members = range(n)
    teams = itertools.combinations(members, count)
    members = set(members)
    min_result = 9999999

    for team in teams:
        start = set(list(team))
        link = list(members - start)
        start_total = 0
        link_total = 0

        # devide in half by containing 0 or not.
        if team[0] != 0:
            break

        start = list(start)
        # itertools return result by the generator object.
        start_combi = itertools.combinations(start, 2)
        for coms in start_combi:
            start_total += cal(lines, coms[0], coms[1])

        link_combi = itertools.combinations(link, 2)
        for coml in link_combi:
            link_total += cal(lines, coml[0], coml[1])

        if abs(link_total - start_total) < min_result:
            min_result = abs(link_total - start_total)

    return min_result


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        line = list(map(int, sys.stdin.readline().strip().split()))
        lines.append(line)

    # the stats are collected in one place, so that you can be retrieved only once.
    for i in range(n):
        for j in range(n):
            if j > i:
                lines[i][j] = lines[i][j] + lines[j][i]
                lines[j][i] = 0
    print(bruteforce(lines, n))