"""
백준 7576. 토마토
blog : https://daimhada.tistory.com/83
problem : https://www.acmicpc.net/problem/7576
"""


def solve(farm, tomatos, tcount, nycount):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    changed = True
    changed_count = 0
    while changed:
        next_tomatos = []
        changed_count += 1
        changed = False
        while tomatos:
            tomato = tomatos.pop()
            x, y = tomato
            for i in range(4):
                temp_x = x + dx[i]
                temp_y = y + dy[i]
                if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= m:
                    continue
                value = farm[temp_x][temp_y]
                # change status if raw tomato is
                if value == 0:
                    changed = True
                    nycount -= 1
                    # All raw tomatoes are changed
                    if nycount == 0:
                        return changed_count

                    farm[temp_x][temp_y] = 1
                    # Next check list of tomatos
                    next_tomatos.append((temp_x, temp_y))
        tomatos = next_tomatos
    return -1

if __name__ == "__main__":
    m, n = map(int, input().strip().split())
    lines = []
    tomato = []
    tomato_count = 0
    notyet_count = 0
    empty_count = 0
    for i in range(n):
        line = list(map(int, input().strip().split()))
        lines.append(line)

    for i in range(n):
        for j in range(m):
            value = lines[i][j]
            if value == 0:
                notyet_count += 1
            elif value == 1:
                tomato_count += 1
                tomato.append((i, j))
            elif value == -1:
                empty_count += 1

    if tomato_count == 0:
        print(-1)
    elif (tomato_count + empty_count) == (n*m):
        print(0)
    else:
        print(solve(lines, tomato, tomato_count, notyet_count))
