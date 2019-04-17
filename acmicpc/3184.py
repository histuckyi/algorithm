
"""
백준 3194. 양
blog : https://daimhada.tistory.com/137
problem : https://www.acmicpc.net/problem/3184
"""
import sys
input = sys.stdin.readline


def solve(n, m, field):
    visited = [[False] * m for j in range(n)]
    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]
    total_sheep = 0
    total_wolf = 0

    for i in range(n*m):
        cur_r = i // m
        cur_c = i % m
        value = field[cur_r][cur_c]

        # 양과 늑대의 수를 센다.
        if value == 'v':
            total_wolf += 1
        elif value == 'o':
            total_sheep += 1


        # 방문하지 않은 늑대칸 발견
        if  not visited[cur_r][cur_c] and value == 'v':
            around_pos = []
            around_pos.append((cur_r,cur_c))
            visited[cur_r][cur_c] = True  # 방문 표시

            wolf = 0
            sheep = 0
            while around_pos:
                pos = around_pos.pop()
                r, c = pos

                v = field[r][c]

                if v == 'o': # 양
                    sheep += 1
                elif v == 'v': # 늑대
                    wolf += 1
                elif v == '#': # 울타리
                    continue

                # 상하좌우 체크
                for d in range(4):
                    temp_r = r + dr[d]
                    temp_c = c + dc[d]

                    # 범위 초과
                    if temp_r < 0 or temp_c < 0 or n <= temp_r or m <= temp_c:
                        continue

                    # 벽이거나 이미 방문한 곳
                    if field[temp_r][temp_c] == '#' or visited[temp_r][temp_c]:
                        continue

                    visited[temp_r][temp_c] = True  # 방문 표시
                    around_pos.append((temp_r, temp_c))

            # 양과 늑대 중 진 종족의 수를 전체 수에서 차감
            if wolf < sheep:
                total_wolf -= wolf
            else:
                total_sheep -= sheep
    return total_sheep, total_wolf




if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    field = []
    for i in range(n):
        field.append(list(input().strip()))

    s, w = solve(n, m , field)
    print("{0} {1}".format(s, w))




