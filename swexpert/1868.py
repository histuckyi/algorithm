"""
SW Expert Academy 1868. 파핑파핑 지뢰찾기(D4)
blog : https://daimhada.tistory.com/68
"""
def checkAroundPos(arr, aroundPos):
    """
    Count the number of bomb, while pushing positions around pos
    if it is bomb, don't explore anymore
    """
    dx = [1, -1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 1, -1, -1, 1, -1, 1]

    while aroundPos:
        # pos that needs to be checked around
        x,y = aroundPos.pop(0)
        count = 0
        temp_around = []

        # only normal position
        if arr[x][y] != '.':
            continue

        for i in range(8):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < n:
                value = arr[temp_x][temp_y]
                if value == "*":
                    count += 1
                elif value == ".":
                    temp_around.append((temp_x,temp_y))
        arr[x][y] = count
        # check temp_around if the is no bomb around pos
        if count == 0:
            aroundPos += temp_around

def solve(arr, n):
    dx = [1, -1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 1, -1, -1, 1, -1, 1]
    click_count = 0

    # fist traversal
    # check pos with no bomb position first.
    for i in range(0, n*n):
        next_pos = False
        x, y = i // n, i % n

        if arr[x][y] != '.':
            continue

        aroundPos = []
        for d in range(8):
            temp_x = x + dx[d]
            temp_y = y + dy[d]
            # check if it is bomb
            if temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < n:
                # bomb
                if arr[temp_x][temp_y] == '*':
                    next_pos = True
                    break
                else:
                    aroundPos.append((temp_x, temp_y))
        if next_pos:
            continue

        # click if all sides are not bomb
        click_count += 1
        arr[x][y] = 0
        # 주변 탐색
        checkAroundPos(arr, aroundPos)

    # second traversal
    # count extra positions(no bomb, and remaining position)
    for i in range(0, n*n):
        x, y = i // n, i % n
        if arr[x][y] == '.':
            click_count += 1

    return click_count


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = []
        for j in range(n):
            arr.append(list(input().strip()))
        print('#{0} {1}'.format(t+1, solve(arr, n)))
