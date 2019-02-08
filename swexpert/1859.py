"""
SW Expert Academy 1859. 백만장자 프로젝트(D2)
blog : https://daimhada.tistory.com/27
"""

def maxValueIndex(start_idx, end_idx, array):
    tempArray = array[start_idx : end_idx + 1]
    return start_idx + tempArray.index(max(tempArray))

def solve(count, array):
    start_index = 0
    end_index = count - 1
    profit = 0

    # reviewing to the last index
    while start_index < end_index:
        payment = 0
        count = 0

        max_index = maxValueIndex(start_index, end_index, array)
        # case 1. If the maximum selling price is start_index, go to the next index
        if max_index == start_index:
            start_index += 1
            continue

        # case 2. If the maximum selling price is not start_index
        for i in range(start_index, max_index):
            payment += array[i]
            count += 1
        profit += (array[max_index] * count - payment)
        start_index = max_index + 1
    return profit

def gens():
    t = int(input())
    for i in range(t):
        count = int(input())
        yield count, list(map(int, input().strip().split()))

if __name__ == "__main__":
    num = 0
    for count, array in gens():
        num += 1
        print('#{0} {1}'.format(num, solve(count, array)))

