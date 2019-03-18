
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

next_color_0 = (0,0)
next_color_1 = (0,0)
color_0_count = 0
color_1_count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def next_pos(visited):
    global n
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                return (i,j)
    return False

def dfs(type, start, end, lines, visited):
    global next_color_0, next_color_1
    global color_0_count, color_1_count
    global dx, dy


    x, y = start
    # check visited position
    visited[x][y] = 1
    if type == 0:
        color_0_count += 1
    elif type == 1:
        color_1_count += 1

    current_color = lines[x][y]

    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        if temp_x < 0 or temp_y < 0 or n <= temp_x or n <= temp_y or visited[temp_x][temp_y] != -1:
            continue

        next_color = lines[temp_x][temp_y]

        # normal
        if type == 0:
            if current_color == next_color:
                dfs(0, (temp_x, temp_y), end, lines, visited)
            else:
                next_color_0 = (temp_x, temp_y)
        # unnormal
        else:
            if (current_color == next_color) or \
                ((current_color == "G" or current_color == "R") and (next_color == "G" or next_color == "R")):
                dfs(1, (temp_x, temp_y), end, lines, visited)
            else:
                next_color_1 = (temp_x, temp_y)

if __name__ == "__main__":
    n = int(input().strip())
    lines = []
    for i in range(n):
        line = list(input().strip())
        lines.append(line)

    visited_0 = [[-1]*n for j in range(n)]
    visited_1 = [[-1]*n for j in range(n)]

    count_0, count_1 = 0, 0
    while color_0_count < n*n:
        next_x, next_y = next_color_0
        if visited_0[next_x][next_y]:
            next_color_0 = next_pos(visited_0)
        dfs(0, next_color_0, (n-1, n-1), lines, visited_0)
        count_0 += 1

    while color_1_count < n*n:
        next_x, next_y = next_color_1
        if visited_1[next_x][next_y]:
            next_color_1 = next_pos(visited_1)
        dfs(1, next_color_1, (n-1, n-1), lines, visited_1)
        count_1 += 1

    print("{0} {1}".format(count_0, count_1))

"""
10
RRRRRRRRRR
RGGGGGGGGR
RGRRRRRRGR
RGRGGGGRGR
RGRGRRGRGR
RGRGRRGRGR
RGRGGGGRGR
RGRRRRRRGR
RGGGGGGGGR
RRRRRRRRRR

100
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
RGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRG
GRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGRGR
"""