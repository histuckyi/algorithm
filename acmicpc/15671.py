"""
백준 15671. 오델로
blog : https://daimhada.tistory.com/58
problem : https://www.acmicpc.net/problem/15671
"""

import sys
input = sys.stdin.readline

def changeArr(arr, color_list, pos, color):
    r, c = pos
    changed = set()
    changed.add((r, c))
    for po in color_list:
        pr, pc = po[0], po[1]
        temp = set() # Add stones to be changed

        # Check for horizontal, vertical and diagonal stones
        #existing stone(po) moves to the position of the new one(r,c)
        if pr == r:
            count = abs(pc - c) - 1
            # Position on the same horizontal line
            # Add or subtract 1 to the number of pc(po[1]) to be c.
            while count:
                count -= 1
                if pc > c:
                    pc -= 1
                else:
                    pc += 1
                # Range check (Unneessary, already 'count' value has checked)
                if pc < 0 or pc > 5:
                    temp = set()
                    break
                # if stones is my color, undo updating
                if arr[r][pc] == color:
                    temp = set()
                    break
                # if place is empty, undo updating
                if arr[r][pc] == '.':
                    temp = set()
                    break
                # Save stones you might have changed
                temp.add((r, pc))
            changed.update(temp) # Add to stone list to change
        elif pc == c:
            count = abs(pr - r) - 1
            # Position in the same vertical lines.
            # Add or subtract 1 to the number of pr(po[0]) to be r.
            while count:
                count -= 1
                if pr > r:
                    pr -= 1
                else:
                    pr += 1
                if pr < 0 or pr > 5:
                    temp = set()
                    break
                if arr[pr][c] == color:
                    temp = set()
                    break
                if arr[pr][c] == '.':
                    temp = set()
                    break
                temp.add((pr,c))
            changed.update(temp)
        elif abs(pr - r) == abs(pc - c) and abs(pc - c) > 1:
            # Stone located diagonally
            # Move the existing stone(po) diagonally to the new stone.
            count = abs(pr - r) - 1

            if pr > r:
                # Existing stone(po) are located below new stones(r,c)(pr -= 1)
                if pc > c:
                    # Existing stone(po) are located to the right of the new stone(r,c), pc -= 1
                    while count:
                        pr -= 1
                        pc -= 1
                        count -= 1
                        if pr < 0 or pc < 0 or pr > 5 or pc > 5:
                            temp = set()
                            break
                        if arr[pr][pc] == color:
                            temp = set()
                            break
                        if arr[pr][pc] == '.':
                            temp = set()
                            break
                        temp.add((pr, pc))
                    changed.update(temp)
                else:
                    # Existing stone(po) are located to the left of the new stone(r,c), pc += 1
                    while count:
                        pr -= 1
                        pc += 1
                        count -= 1
                        if pr < 0 or pc < 0 or pr > 5 or pc > 5:
                            temp = set()
                            break
                        if arr[pr][pc] == color:
                            temp = set()
                            break
                        if arr[pr][pc] == '.':
                            temp = set()
                            break
                        temp.add((pr, pc))
                    changed.update(temp)
            else:
                # Existing stone(po) are located above new stone(r,c) (pr += 1)
                if pc > c:
                    # Existing stone(po) are located on the right side of the new stone(pc -= 1)
                    while count:
                        pr += 1
                        pc -= 1
                        count -= 1
                        if pr < 0 or pc < 0 or pr > 5 or pc > 5:
                            temp = set()
                            break
                        if arr[pr][pc] == color:
                            temp = set()
                            break
                        if arr[pr][pc] == '.':
                            temp = set()
                            break
                        temp.add((pr, pc))
                    changed.update(temp)
                else:
                    # Existing stone(po) are located on the left side of the new stone(pc += 1)
                    while count:
                        pr += 1
                        pc += 1
                        count -= 1
                        if pr < 0 or pc < 0 or pr > 5 or pc > 5:
                            temp = set()
                            break
                        if arr[pr][pc] == color:
                            temp = set()
                            break
                        if arr[pr][pc] == '.':
                            temp = set()
                            break
                        temp.add((pr,pc))
                    changed.update(temp)
    return changed

def solve(posList, arr):
    # setting
    black_list = set()
    white_list = set()

    r = (6//2) - 1
    white_list.update([(r,r),(r+1, r+1)])
    black_list.update([(r+1,r),(r, r+1)])
    arrList[r][r], arrList[r+1][r+1] = 'W', 'W'
    arrList[r+1][r], arrList[r][r+1] = 'B', 'B'

    # posList is a list of new stones.
    # Check one by one to compare the position of the existing stone with new one(from posList).
    for position in posList:
        color = position[1]
        pos = position[0]
        color_list = white_list

        if color == "B":
            color_list = black_list

        # Changed is the stone position list
        # (new position & opponent position to turn over)
        changed = changeArr(arr, color_list, pos, color)

        for p in changed:
            arr[p[0]][p[1]] = color

        # Record the stone position to the black/white list
        if color == "B":
            black_list.update(changed)
            white_list.difference_update(changed)

        else:
            white_list.update(changed)
            black_list.difference_update(changed)

    # output
    for li in arr:
        print("".join(li))

    # output
    if len(black_list) > len(white_list):
        print("Black")
    else:
        print("White")


if __name__ == "__main__":
    n = int(input().strip())  # log count
    arrList = [["."]*6 for i in range(6)]

    # Black stone is first.
    posList = []
    for i in range(n):
        color = "W" # white
        if (i % 2) == 0:
            color = "B" # black
        r,c = map(int, input().strip().split())
        pos = ((r - 1, c - 1), color)
        posList.append(pos)

    solve(posList, arrList)
