"""
SW Expert Academy 4613. 러시아 국기 같은 깃발(D4)
blog : https://daimhada.tistory.com/61
"""

def solve(_n, _m, map):
    # ‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색
    # 맨 위, 맨 아래에는 이미 색이 정해져 있다.
    extra_count = _n - 2

    result = 99999999999
    for wnb in range(1, extra_count + 1):
        for j in range(1, wnb + 1):
            total = 0
            bc = j
            rc = extra_count - wnb
            wc = wnb - bc

            # 맨 위, 아래 칠할 수를 더해준다.
            wc += 1
            rc += 1

            # 흰색으로 wc 만큼 칠하기
            for wi in range(0, wc):
                total += map[wi][0]

            # 파란색으로 bc 만큼 칠하기
            for bi in range(wc, wc + bc):
                total += map[bi][1]

            # 빨간색으로 rc 만큼 칠하기
            for ri in range(wc+ bc,wc + bc + rc):
                total += map[ri][2]
            if result > total:
                result = total
    return result

if __name__ == "__main__":
    t = int(input().strip())

    for i1 in range(t):
        n,m = map(int, input().strip().split())
        lines = []
        for i2 in range(n):
            line = list(input().strip())
            # 각 색을 칠했을 때 새로 칠해야 하는 칸의 수를 구한다
            w = m - line.count('W')
            b = m - line.count('B')
            r = m - line.count('R')
            lines.append((w,b,r))
        count = solve(n, m, lines)
        print("#{0} {1}".format(i1+1, count))

