"""
SW Expert Academy 1961. 숫자 배열 회전
blog : https://daimhada.tistory.com/61
"""

def solve(case, n, rotation_map):
    result = [[] for i in range(n)]
    # Rotate 3 times in total
    for count in range(3):
        new_map = []
        index = 0
        for z in zip(*rotation_map):
            new_map.append(list(reversed(z)))
            result[index].append(''.join(list(reversed(z))))
            index += 1
        rotation_map = new_map

    print('#{0}'.format(case))
    for w in result:
        print(' '.join(w))

if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        lines = []
        n = int(input())
        for j in range(n):
            line = list(map(str, input().strip().split()))
            lines.append(line)
        solve(i + 1, n, lines)
