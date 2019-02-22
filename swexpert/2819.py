"""
SW Expert Academy 2819. 격자판의 숫자 이어 붙이
blog : https://daimhada.tistory.com/67
"""

number_set = set()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
string = ''
pos_list = []

def explore(start, count):
    global string
    global before_pos
    global pos_list

    x, y = start
    # Complete string number
    if count == 0:
        number_set.add(string)
        return

    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        if temp_x >= 0 and temp_y >= 0 and temp_x < 4 and temp_y < 4:
            string += str(array[temp_x][temp_y])
            pos_list.append((temp_x,temp_y))
            # Next destnation
            explore((temp_x, temp_y), count - 1)
            # Change last position
            string = string[:-1]
            # Delete last position
            pos_list.pop(-1)

def solve():
    global string
    global pos_list
    # Set start position
    for i in range(0, 16):
        pos_list = []
        string += str(array[i // 4][i % 4])
        pos_list.append((i//4, i%4))
        explore((i//4, i%4), 6)
        string = ''
    return len(number_set)

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        # Initialization
        array = []
        number_set = set()
        pos_list = []
        string = ''

        for j in range(4):
            array.append(list(map(int, input().strip().split())))
        result = solve()
        print('#{0} {1}'.format(tc + 1, result))