"""
SW Expert Academy 1208. Flatten(D3)
blog : https://daimhada.tistory.com/28
"""
max = 100

# dict : count per level(층 별 박스 수)
def calcualteBoxCount(dict, level):
    for i in range(1, level + 1):
        if str(i) in dict:
            dict[str(i)] += 1
        else:
            dict[str(i)] = 1

def solve(dump_count, cargo):
    global max
    count_per_level = {}
    top = 0 # top level
    chk_bottom = 1 # check bottom level
    bottom = 1 # full lower floor(level)

    for level in cargo:
        # Store the highest number of stacked boxes
        if level > top:
            top = level
        calcualteBoxCount(count_per_level, level)

    #dump
    while dump_count:
        box_count = count_per_level[str(top)] # Number of boxes placed on the top floor
        vacancy = max - count_per_level[str(chk_bottom)] # Number of remaining spaces

        # If the lowest layer is full, check the next lowest empty space
        if vacancy == 0:
            bottom = chk_bottom
            del count_per_level[str(chk_bottom)]  # Clear the bottom floor
            if top <= chk_bottom + 1:
                break
            else:
                chk_bottom += 1
                continue

        # If the top layer is full, stop the dump.
        if box_count == max:
            break

        # Determine the number of boxes to move. (The number of boxes to move does not exceed dump_count)
        if dump_count < box_count:
            box_count = dump_count
        result = box_count - vacancy

        # case 1. Number of boxes to move == Number of empty spaces
        if result == 0:
            dump_count -= box_count # the number of boxes moved
            count_per_level[str(top)] -= box_count
            count_per_level[str(chk_bottom)] += box_count
            del count_per_level[str(chk_bottom)]  # Delete filled bottoms
            bottom = chk_bottom  # Record the lowest filled

            # Check if all top floors are empty
            if count_per_level[str(top)] == 0:
                del count_per_level[str(top)]
                # Decrease the top value so that you can see if there is a box to move to on the next floor
                top -= 1
            if top <= chk_bottom + 1:
                break
            # Increase the value of chk_bottom to see if there is room on the next floor.
            chk_bottom += 1

        # case 2. Number of boxes to move> Number of empty spaces (positive number)
        if result > 0:
            dump_count -= vacancy
            count_per_level[str(top)] -= vacancy # move the box
            count_per_level[str(chk_bottom)] += vacancy # Fill the empty space
            del count_per_level[str(chk_bottom)] # Delete filled bottoms
            bottom = chk_bottom
            if top <= chk_bottom + 1:
                break
            # Make sure there is free space on the upper floor.
            chk_bottom += 1

        # case 3. Number of boxes to move < Number of empty spaces (negative number)
        if result < 0:
            dump_count -= box_count
            count_per_level[str(chk_bottom)] += box_count # fill the empty spaces.
            count_per_level[str(top)] -= box_count
            # 항상 최상위층이 비워지는 건 아니다, dump_count의 수에 따라서 안비워질수도 있음
            #The top level is not always emptied,just depending on the number of dump_count
            if count_per_level[str(top)] == 0:
                del count_per_level[str(top)]
                # Decrease the top value, so that you can check if there is a box to move to other floor.
                top -= 1
            if top <= bottom:
                break
    return top - bottom

def gens():
    for i in range(10):
        dump_count = int(input())
        yield dump_count, list(map(int, input().strip().split()))

if __name__ == "__main__":
    num = 0
    for dump_count, cargo in gens():
        num += 1
        print('#{0} {1}'.format(num, solve(dump_count, cargo)))


