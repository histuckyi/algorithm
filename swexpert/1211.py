
"""
SW Expert Academy 1211.Ladder2 (D4)
blog : https://daimhada.tistory.com/84
"""
def solve(ladder):
    start_list = []
    for i in range(99, -1, -1):
        if ladder[99][i] == 1:
            start_list.append((99, i))

    left = (0, -1)
    right = (0, 1)
    up = (-1, 0)
    min_count = 99999
    min_y = None
    while start_list:
        start_x, start_y = start_list.pop()
        next_check_direction = [left, right, up]
        count = 1
        while start_x > 0:
            count += 1
            add_x = 0
            add_y = 0
            for dir in next_check_direction:
                if checkPosition(ladder, (start_x, start_y), dir):
                    if dir == left:
                        start_y -= 1
                        next_check_direction = [left, up]
                    elif dir == right:
                        start_y += 1
                        next_check_direction = [right, up]
                    else:
                        start_x -= 1
                        next_check_direction = [left, right, up]
                    break
        if count < min_count:
            min_count = count
            min_y = start_y
    return min_y


# if it is route, return True
def checkPosition(ladder, current_pos, dir):
    x, y = current_pos
    temp_x = x + dir[0]
    temp_y = y + dir[1]
    if temp_x < 0 or temp_y < 0 or temp_x >= 100 or temp_y >= 100:
        return False
    if ladder[temp_x][temp_y] == 0:
        return False
    return True


def gen():
    lines = []
    for i in range(100):
        line = list(map(int, input().strip().split()))
        lines.append(line)
    yield lines

if __name__ == "__main__":
    for j in range(10):
        t = int(input())
        for lines in gen():
            result = solve(lines)
            print("#{0} {1}".format(t, result))