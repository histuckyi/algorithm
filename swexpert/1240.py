
def solve(code):
    code_table = {
        "3211" : 0,
        "2221" : 1,
        "2122" : 2,
        "1411" : 3,
        "1132" : 4,
        "1231" : 5,
        "1114" : 6,
        "1312" : 7,
        "1213" : 8,
        "3112" : 9
    }

    # Find the first index of crypto code
    # 1) flip the list with the crypto code
    # 2) find the index where the first '1' is, subtract (index - 1) from the total length
    # * list.index(value) : return the fisrt index of the value
    reversed_t = list(reversed(code))
    real_index = len(code) - (reversed_t.index('1') - 1)
    start_index = real_index - 55
    line = ''
    compared = '0'
    count = 0

    # 코드만 추출
    for ch in code[start_index:start_index + 56]:

        if ch == compared:
            count += 1
        else:
            line += str(count)
            compared = ch # change character to compare
            count = 1

    # Add count for last character
    line += str(count)

    number = []
    for idx in range(0, 32, 4):
        number.append(code_table[line[idx:idx + 4]])

    # Check if crypto code is correct
    hol = (number[0] + number[2] + number[4] + number[6])*3
    zz = number[1] + number[3] + number[5] + number[7]
    if (hol + zz) % 10 == 0:
        numbers = list(map(int, list(number)))
        return sum(numbers)
    else:
        return 0

def findLine(n):
    result = None
    for i in range(n):
        temp = list(input().strip())
        if temp.count('1') > 1:
            result = temp
    return result

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        # n줄에 m개
        n, m = map(int, input().strip().split())
        c = findLine(n)
        print("#{0} {1}".format(i+1, solve(c)))
