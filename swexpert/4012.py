"""
SW Expert Academy 4012. 요리사
blog : https://daimhada.tistory.com/47

 pool = ['A', 'B', 'C']
 print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
 print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
"""
import itertools

def cal(lines, a, b):
    return lines[int(a)][int(b)]

def bruteforce(lines, n):
    count = n // 2
    incredients = range(n)
    combis = itertools.combinations(incredients, count)
    incredients = set(incredients)
    min_result = 9999999

    for combi in combis:
        afood = set(list(combi))
        bfood = list(incredients - afood)
        afood_total = 0
        bfood_total = 0

        # devide in half by containing 0 or not.
        if combi[0] != 0:
            break

        afood = list(afood)
        # itertools return result by the generator object.
        afood_combi = itertools.combinations(afood, 2)
        for coma in afood_combi:
            afood_total += cal(lines, coma[0], coma[1])

        bfood_combi = itertools.combinations(bfood, 2)
        for comb in bfood_combi:
            bfood_total += cal(lines, comb[0], comb[1])

        if abs(afood_total - bfood_total) < min_result:
            min_result = abs(afood_total - bfood_total)

    return min_result


if __name__ == "__main__":
    c = int(input().strip())
    for t in range(c):
        n = int(input().strip())
        lines = []
        for i in range(n):
            line = list(map(int, input().strip().split()))
            lines.append(line)

        # the stats are collected in one place, so that you can be retrieved only once.
        for i in range(n):
            for j in range(n):
                if j > i:
                    lines[i][j] = lines[i][j] + lines[j][i]
                    lines[j][i] = 0
        print('#{0} {1}'.format(t + 1, bruteforce(lines,n)))