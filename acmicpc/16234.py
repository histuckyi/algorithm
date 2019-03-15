"""
백준 16234. 인구이동
blog : https://daimhada.tistory.com/92
problem : https://www.acmicpc.net/problem/14501
"""

import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def nextStart(n, visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                return (i, j)
    return False


def checkrange(frist_v, second_v,  l, r):
    value = abs(frist_v - second_v)
    if l <= value <= r:
        return True
    return False

def union(n, l, r, visited, ground):
    country = n*n
    startPoint = [(0, 0)]
    union_num= 0
    union_count = 0
    flag = True
    # Save Population number to Renew
    arr = []
    immigration_count = 0
    next_pos = None


    while flag:
        # total union people count
        total = 0
        # number of union country
        count = 0

        # find union country
        while startPoint:
            pos = startPoint.pop()
            x, y = pos
            visited[x][y] = union_num
            frist_value = ground[x][y]
            total += frist_value
            count += 1
            country -= 1 # number of unchecked country

            for i in range(4):
                temp_x = pos[0] + dx[i]
                temp_y = pos[1] + dy[i]
                # Out of range and already visited
                if temp_x < 0 or temp_y < 0 or n <= temp_x or n <= temp_y or visited[temp_x][temp_y] != -1:
                    continue
                second_value = ground[temp_x][temp_y]
                # condition check
                if checkrange(frist_value, second_value, l, r):
                    visited[temp_x][temp_y] = union_num
                    startPoint.append((temp_x, temp_y))
                else:
                    #next starting point
                    if i == 3 and len(startPoint) == 0:
                        next_pos = (temp_x, temp_y)

        new_value = total // count
        arr.append(new_value)
        union_num+= 1
        union_count += 1

        if country == 0:
            # No union
            if union_count == n*n:
                flag = False
                break
            #  All country united
            if union_count == 1:
                flag = False
                immigration_count += 1
                break

            # update value
            for i1 in range(n):
                for j1 in range(n):
                    # Get people count
                    index = visited[i1][j1]
                    visited[i1][j1] = -1
                    ground[i1][j1] = arr[index]

            # init
            country = n * n
            startPoint = [(0, 0)]
            union_num = 0 # union number
            union_count = 0
            immigration_count += 1
            arr = []
        else:
            if next_pos:
                startPoint.append(next_pos)
                # init
                next_pos = None
            else:
                # next start position
                startPoint.append(nextStart(n, visited))

    return immigration_count

def solve(n, l, r, ground):
    visited = [[-1]*n for i in range(n)]
    return union(n, l, r, visited, ground)


if __name__ == "__main__":
    n, l, r = map(int, input().strip().split())
    ground = []
    for i in range(n):
        land = list(map(int, input().strip().split()))
        ground.append(land)
    print(solve(n, l, r, ground))