"""
백준 2178. 미로탐색
blog : https://daimhada.tistory.com/82
problem : https://www.acmicpc.net/problem/2178
"""

def solve(start, goal, lines):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    next_pos = []
    next_pos.append(start)
    while next_pos:
        x, y = next_pos.pop(0)
        value = lines[x][y]
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= m:
                continue
            
            temp_value = lines[temp_x][temp_y]

            # Wall
            if temp_value < 1:
                continue

            # change values of value + 1 and temp_value
            # if current value + 1 is lee than temp_value
            if temp_value == 1 or value + 1 < temp_value:
                lines[temp_x][temp_y] = value + 1
                next_pos.append((temp_x, temp_y))
    return lines[goal[0]][goal[1]]

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    lines = []
    for i in range(n):
        line = list(map(int, list(input().strip())))
        lines.append(line)
    start = (0, 0)
    goal = (n-1, m-1)
    print(solve(start, goal, lines))
    