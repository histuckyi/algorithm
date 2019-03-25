"""
백준 14890. 경사로
blog : https://daimhada.tistory.com/111
problem : https://www.acmicpc.net/problem/14890
"""

import sys
input = sys.stdin.readline

def solve(n, l, board):
    zip_board = list(map(list, list(zip(*board))))
    count1 = counting(n, l, zip_board)
    count2 = counting(n, l, board)
    return count1 + count2

def counting(n, l, board):
    count = 0
    for i in range(n):
        continued = 0
        prev_height = -1
        cur_height = -1
        checked = False

        for j in range(n):
            cur_height = board[i][j]

            # same height
            if 0 <= prev_height and prev_height != cur_height:

                if checked:
                    if l == continued:
                        continued = 1
                        checked = False
                        continue
                    else:
                        break

                # Height difference
                gap = prev_height - cur_height

                # gap is more than 1 (ramp x)
                if abs(gap) != 1:
                    break

                # case2, Ascending ramp
                if gap < 0:
                    if l <= continued:
                        # 현재부터 다시 같은 높이의 칸을 센다
                        continued = 1
                    else:
                        break
                # case1, descending ramp
                else:
                    continued = 1
                    checked = True
                    if l == continued:
                        continued = 0
                        checked = False
            else:
                continued += 1
                if checked:
                    if l == continued:
                        continued = 0
                        checked = False

            prev_height = cur_height
        else:
            # 경사로를 놓을 수 있는지 체크 중이 아닌 경우만 길로 체크
            # count if not you are doing check L
            if not checked:
                count += 1
    return count


if __name__ == "__main__":
    n, l = map(int, input().strip().split())
    board = []
    for i in range(n):
        board.append(list(map(int, input().strip().split())))
    print(solve(n, l, board))