"""
SW Expert Academy 1954. 달팽이 숫자
blog : https://daimhada.tistory.com/77
"""

def solve(n):
    # right, down, left, up
    direction_list = [(0,1), (1, 0), (0, -1), (-1, 0)]
    num = 0
    direction_index = 0
    current_r, current_c = 0, -1
    array = [[-1]*n for i in range(n)]

    while num < n*n:
        dir = direction_list[direction_index]
        temp_r = current_r + dir[0]
        temp_c = current_c + dir[1]

        # 범위 초과시 방향을 바꾼다
        if temp_c < 0 or temp_r < 0 or temp_c >= n or temp_r >= n or array[temp_r][temp_c] != -1:
            direction_index += 1
            if direction_index == 4:
                direction_index = 0
        else:
            num += 1
            current_r, current_c= temp_r, temp_c
            array[current_r][current_c] = num

    return array


if __name__ == "__main__":
    t = int(input())
    for c in range(t):
        n = int(input())
        print("#{0}".format(c+1))
        result = solve(n)
        for line in result:
            print(' '.join(map(str,line)))

