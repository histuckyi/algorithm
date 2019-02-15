"""
SW Expert Academy 4613. 러시아 국기 같은 깃발(D4)
blog : https://daimhada.tistory.com/61
"""

def solve(_n, _m, map):
    # ‘W’: white, ‘B’: blue, ‘R’: red
    # The color are already set at the top and bottom
    extra_count = _n - 2

    result = 99999999999
    for wnb in range(1, extra_count + 1):
        for j in range(1, wnb + 1):
            total = 0
            bc = j
            rc = extra_count - wnb
            wc = wnb - bc

            # set at the top and bottom
            wc += 1
            rc += 1

            # fill wc lines in white
            for wi in range(0, wc):
                total += map[wi][0]

            # fill bc lines in blue
            for bi in range(wc, wc + bc):
                total += map[bi][1]

            # fill rc lines in blue
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
            # Calculate the count of spaces that need to be filled in each color
            w = m - line.count('W')
            b = m - line.count('B')
            r = m - line.count('R')
            lines.append((w,b,r))
        count = solve(n, m, lines)
        print("#{0} {1}".format(i1+1, count))

