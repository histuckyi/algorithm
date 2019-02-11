"""
LeetCode 6. ZigZag Conversion
blog : https://daimhada.tistory.com/54
problem : https://leetcode.com/problems/zigzag-conversion/
"""

def convert(s, numRows):
    lines = ['' for i in range(numRows)]
    flag = True
    down_index = [n for n in range(numRows)]
    up_index = [n for n in range(numRows - 2, 0, -1)]
    while True and flag:
        for di in down_index:
            if not len(s):
                flag = False
                break
            lines[di] += s[0]
            s = s[1:]
        for di in up_index:
            if not len(s):
                flag = False
                break
            lines[di] += s[0]
            s = s[1:]
    return ''.join(lines)


print(convert('PAYPALISHIRING', 3))  # PAHNAPLSIIGYIR
print(convert('PAYPALISHIRING', 4))  # PINALSIGYAHRPI