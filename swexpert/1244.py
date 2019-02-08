"""
SW Expert Academy 1244. 최대 상금(D3)
blog : https://daimhada.tistory.com/49
"""
def gen(n):
    for i in range(n):
        yield input().strip().split()

def solve(n, count):
    number = list(map(int, n))
    # Change flag to False if you need to stop the loop.
    flag = True
    checkIndex = 0 # Index from the beginning
    targetIndex = -1 # Index to exchange
    lastIndex = len(number) - 1
    while count and flag:
        chk = number[checkIndex]
       # Check whether the target exceeds the range of numbers
        if checkIndex + 1 < lastIndex:
            other = max(number[checkIndex + 1:])
            otherCount = number.count(other)
            # Compare the value of checkIndex with the maximum value from behind
            if chk < other:
                changeLen = 0
                # Check index of target from behind
                for i in range(lastIndex, 0, -1):
                    if number[i] == other:
                        targetIndex = i
                        break
                # targetIndex의 값이 여러개인 경우 연속되어 있는지 체크 ex) (32)8(88) -> (88)8(32)
                # Check if there are multiple values of targetIndex in succession
                if otherCount > 1:
                    for i in range(checkIndex, lastIndex):
                        if number[checkIndex] >= number[i]:
                            changeLen += 1
                        else:
                            break
                    # 변경할 길이는 checkIndex 부분의 감소하는 값들의 갯수, 뒷자리의 연속된 값의 갯수, 교환 가능한 count의 수 중에 최솟값
                    # The length to change is the min value from changeLen, otherCount, count
                    changeLen = min(changeLen, otherCount, count)
                    for i in range(0, changeLen):
                        if number[targetIndex] == number[targetIndex - i]:
                            break
                        else:
                            targetIndex -= 1
                    # Replace entirely from targetIndex to changeLen
                    number = number[0:checkIndex] + number[targetIndex:targetIndex + changeLen]\
                            + number[checkIndex + changeLen:targetIndex] + number[checkIndex:checkIndex + changeLen]\
                            + number[targetIndex + changeLen:]
                    # Subtract the changed length
                    count -= changeLen
                else:
                    number[checkIndex], number[targetIndex] = number[targetIndex] , number[checkIndex]
                    count -= 1
        checkIndex += 1
        # If count remains
        if checkIndex == lastIndex and count > 0:
            # no change because the same place change is possible.
            if count % 2 == 0:
                flag = False
            else:
                # have to change it once
				# If two or more same numbers are side by side : change flag  to False
				# else : Change the value of the last two cards
                for i in number:
                    if number.count(i) >= 2:
                        flag = False
                if flag:
                    number[lastIndex], number[lastIndex -1] = number[lastIndex - 1], number[lastIndex]
                    flag = False
    return ''.join(map(str, number))

num = 0
n = int(input().strip())
for n, count in gen(n):
    num += 1
    print('#{0} {1}'.format(num, solve(list(n), int(count))))