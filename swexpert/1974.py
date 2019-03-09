"""
SW Expert Academy 1974. 스도쿠 검증
blog : https://daimhada.tistory.com/76
"""

def solve(arr):
    for i in range(9):
        # 가로 검증
        if len(set(arr[i])) != 9:
            return 0
        # 세로 검증
        temp = set()
        for j in range(9):
            temp.add(arr[j][i])
        if len(temp) != 9:
            return 0

    lineArray = [set(),set(),set()]
    index = 0
    # 9개의 구역 검사
    for r in range(0, 81):
        x = r // 9
        y = r % 9

        # 3개 구역씩 스도쿠 조건을 확인하고 비워준다
        if r != 0 and r % 27 == 0:
            if len(lineArray[0]) != 9 and len(lineArray[1])  != 9 and len(lineArray) != 9:
                return 0

        # 3개씩 나눠담기
        if r != 0 and r % 3 == 0:
            if index == 2:
                index = -1
            index += 1

        lineArray[index].add(arr[x][y])
    return 1

if __name__ == "__main__":
    tt = int(input())
    for t in range(tt):
        array = []
        for i in range(9):
            line = list(map(int, input().strip().split()))
            array.append(line)
        print("#{0} {1}".format(t+1, solve(array)))
