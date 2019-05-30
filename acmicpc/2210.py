"""
백준 2210. 숫자판 점프
blog : https://daimhada.tistory.com/162
problem : https://www.acmicpc.net/problem/2210
"""

import sys
input = sys.stdin.readline

def checkNumber(board, pos, unique_numbers, current_number, count):
    rd = [-1, 0, 1, 0]
    cd = [0, 1, 0, -1]
    r, c = pos

    for i in range(4):
        temp_r = r + rd[i]
        temp_c = c + cd[i]
        if 0 <= temp_r < 5 and 0 <= temp_c < 5:
            next_number = current_number + str(board[temp_r][temp_c])
            if count == 5:
                unique_numbers.add(next_number)
            else:
                checkNumber(board, (temp_r, temp_c), unique_numbers, next_number, count + 1)



def solve(board):
    unique_numbers = set()
    for i in range(5*5):
        r = i // 5
        c = i % 5
        checkNumber(board, (r,c), unique_numbers, str(board[r][c]), 1)
    total_unique_count = len(unique_numbers)
    print(total_unique_count)


if __name__ == "__main__":
    lines = []
    for i in range(5):
        lines.append(input().strip().split())
    solve(lines)
