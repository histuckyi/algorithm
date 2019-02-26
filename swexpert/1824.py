"""
SW Expert Academy 1824. 혁진이의 프로그램 검증
blog : https://daimhada.tistory.com/78
description : This problem is from SW Expert Academy.
                Therefore, some comments are written in Korean.
"""

# import sys
# sys.setrecursionlimit(100000)

def nextStep(array, visited, dir, num, pos):
    """
    :param dir: current direction ("<", ">", "v", "^")\
    :param visited: data about visiting time (direction, num)
    :param num: current number
    :param pos : current position information (r,c)
    :return: (boolean) Whether it is reachable or not
    """
    while pos:
        letter = array[pos[0]][pos[1]]

        # @ : Suspension of program
        if letter == '@':
            return True

        # 동일한 방문 정보가 있다면 무한 반복이므로 종료
        if (dir, num) in visited[pos[0]][pos[1]]:
            return False
        visited[pos[0]][pos[1]].add((dir, num))

        # ?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다
        if letter == "?":
            # 방금 지나 왔던 길을 제외하고, 이동할 수 있는 모든 경우의 수를 생각한다.
            all = ["<", ">", "v", "^"]
            while all:
                nextdir = all.pop()
                if nextStep(array, visited, nextdir, num, nextPos(nextdir, pos)):
                    return True
        else:
            # 숫자 처리
            # 0~9	메모리에 문자가 나타내는 값을 저장한다.
            if letter.isdigit():
                num = int(letter)

            if letter in ["<", ">", "^", "v"]:
                dir = letter

            # _	: 메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
            if letter == "_":
                if num == 0:
                    dir = ">"
                else:
                    dir = "<"

            # |	: 메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
            if letter == "|":
                if num == 0:
                    dir = "v"
                else:
                    dir = "^"

            # +	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
            if letter == "+":
                if num == 15:
                    num = 0
                else:
                    num += 1

            # -	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다.
            if letter == "-":
                if num == 0:
                    num = 15
                else:
                    num -= 1
            # 다음 방향이 유효한지 확인
            pos = nextPos(dir, pos)

# 다음 pos 정보 반환
def nextPos(dir, current_pos):
    direction = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}
    r,c = current_pos

    tr, tc = direction[dir]
    temp_r = r + tr
    temp_c = c + tc

    # 범위 초과 시 조건에 따라 변경
    if temp_r < 0 or temp_c < 0 or temp_r >= n or temp_c >= m:
        if dir == "<":
            temp_c = m - 1
        elif dir == ">":
            temp_c = 0
        elif dir == "^":
            temp_r = n - 1
        elif dir == "v":
            temp_r = 0
    return (temp_r, temp_c)


def solve(array, visited):
    end = 0
    end_point = []
    for qi in range(n):
        for qv in range(m):
            if array[qi][qv] == '@':
                end += 1
                end_point.append((qi,qv))
    if end < 1:
        return "NO"

    for pos in end_point:
        r, c = pos
        top_and_bottom = [(-1, 0), (1,0)]
        left_and_right = [(0,1),(0,-1)]
        bad_count = 0

        for add in top_and_bottom:
            temp_r = r + add[0]
            temp_c = c + add[1]
            if 0 <= temp_r and 0 <= temp_c and temp_r < n and temp_c < m:
                if array[temp_r][temp_c] in ["<", ">"]:
                    bad_count += 1
                else:
                    bad_count = 0
                    break

        for add2 in left_and_right:
            temp_r = r + add2[0]
            temp_c = c + add2[1]
            if 0 <= temp_r and 0 <= temp_c and temp_r < n and temp_c < m:
                if array[temp_r][temp_c] in ["^", "v"]:
                    bad_count += 1
                else:
                    bad_count = 0
                    break

        # If 4 sides are inaccessible, delete valid end_points
        if bad_count == 4:
            end -= 1

    # Check for accessible end_point
    if end < 1:
        return "NO"

    if nextStep(array, visited, '>', 0, (0,0)):
        return 'YES'
    else:
        return "NO"

if __name__ =="__main__":
    t = int(input())
    for i in range(t):
        array = []
        n, m = map(int, input().strip().split())
        for j in range(n):
            array.append(list(input().strip()))


        visited = []
        for vi in range(n):
            visit = []
            for ic in range(m):
                visit.append([])
            visited.append(visit)
        print("#{0} {1}".format(i+1, solve(array, visited)))

