
"""
SW Expert Academy 1226. 미로2
blog : https://daimhada.tistory.com/88
"""
from collections import deque


def solve(start, goal, lines):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    next_pos = deque([])

    sx, sy = start
    if lines[sx][sy] == 3:
        return True

    next_pos.append(start)
    while next_pos:
        start = next_pos.popleft()
        sx, sy = start

        # already visited
        if lines[sx][sy] == 7:
            continue
        
        lines[sx][sy] = 7

        # check around routes  
        for i in range(4):
            temp_x = sx + dx[i]
            temp_y = sy + dy[i]

            # Out of range
            if temp_x < 0 or temp_y < 0 or temp_x >= 100 or temp_y >= 100:
                continue
            
            value = lines[temp_x][temp_y]
                        
            if value == 3:
                return True

            if value == 7:
                continue

            if value == 0:
                next_pos.append((temp_x, temp_y))
    return False


if __name__ == "__main__":
    for t in range(1, 11):
        input()
        lines = []
        start = None
        goal = None
        result = 0
        for i in range(100):
            line = list(map(int, list(input().strip())))
            lines.append(line)

            if 2 in line:
                start = (i, line.index(2))
            if 3 in line:
                goal = (i, line.index(3))

        visited = []
        if solve(start, goal, lines):
            result = 1
        
        print("#{0} {1}".format(t, result))