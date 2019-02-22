"""
백준 14502. 연구소
blog : https://daimhada.tistory.com/66
problem : https://www.acmicpc.net/problem/14502
"""
import sys
import copy

input = sys.stdin.readline

def spreadVirus(_virusList, c_arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    spread_virus_count = 0
    global safe_area

    while _virusList:
        x, y = _virusList.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and 0 <= ny and nx < n and ny < m:
                if c_arr[nx][ny] == 0:
                    c_arr[nx][ny] = 2
                    spread_virus_count += 1
                    _virusList.add((nx, ny))
    # 3 : Wall count
    # Return the number of safe spaces
    return safe_area - spread_virus_count - 3


def setWall(start, wallCount):
    global maxVal
    global n
    global m

    if wallCount == 0:
        copy_arr = copy.deepcopy(arr)
        copy_virusList = copy.deepcopy(virusList)
        # Spread virus
        sCount = spreadVirus(copy_virusList, copy_arr)
        maxVal = max(sCount, maxVal)
        return

    # Loop from ith element
    for i in range(start, n*m):
        x = i // m
        y = i % m

        if arr[x][y] == 0:
            arr[x][y] = 1 # set the wall to (x,y)
            setWall(i+1, wallCount - 1)
            arr[x][y] = 0 # initialize last position


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    posList = []
    virusList = set()
    arr = []
    maxVal = 0
    safe_area = 0

    for i in range(n):
        arr.append(list(map(int, input().strip().split())))

    for i in range(n):
        for j in range(m):
            v = arr[i][j]
            if v == 2:
                virusList.add((i,j))
            elif v == 0:
                safe_area += 1
    setWall(0, 3)
    print(maxVal)


