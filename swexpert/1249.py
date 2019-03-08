
from collections import deque

def solve(n, lines):
    visited = [[-1]*n for i in range(n)]
    checkList = deque([(0, 0)])
    visited[0][0] = lines[0][0]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while checkList:
        x, y = checkList.popleft()
        if x == n-1 and y == n-1:
            continue
        current_v = visited[x][y]
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= n:
                continue

            if visited[temp_x][temp_y] == -1 or \
                current_v + lines[temp_x][temp_y] < visited[temp_x][temp_y]:
                visited[temp_x][temp_y] = current_v + lines[temp_x][temp_y]
                checkList.append((temp_x, temp_y))

    return visited[n-1][n-1]


if __name__ == "__main__":
    t = int(input().strip())
    for tc in range(1, t+1):
        n = int(input().strip())
        lines = []
        for i in range(n):
            line = list(map(int, list(input().strip())))
            lines.append(line)
        print("#{0} {1}".format(tc, solve(n, lines)))

