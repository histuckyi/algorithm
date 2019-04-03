"""
LeetCode 13. Roman to Integer (Easy)
blog : https://daimhada.tistory.com/125
problem : https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Runtime : faster than 96.31% of Python3
        Memory Usage : less than 5.05% of Python3
        """

        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, \
                 "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, \
                 "XC": 90, "CD": 400, "CM": 900}

        is_pass = False
        num = 0
        for idx, ch in enumerate(s):

            if is_pass:
                is_pass = False
                continue

            if idx < len(s) - 1:
                if ch == 'I':
                    next_ch = s[idx + 1]
                    if next_ch == 'V':
                        num += 4
                        is_pass = True
                        continue
                    elif next_ch == 'X':
                        num += 9
                        is_pass = True
                        continue

                if ch == "X":
                    next_ch = s[idx + 1]
                    if next_ch == 'L':
                        num += 40
                        is_pass = True
                        continue
                    elif next_ch == "C":
                        num += 90
                        is_pass = True
                        continue

                if ch == 'C':
                    next_ch = s[idx + 1]
                    if next_ch == 'D':
                        num += 400
                        is_pass = True
                        continue
                    elif next_ch == "M":
                        num += 900
                        is_pass = True
                        continue
            num += table[ch]
        return num


s = Solution()
s.romanToInt("III") # 3
s.romanToInt("IV") # 4
s.romanToInt("IX") # 9
s.romanToInt("LVIII") # 58
s.romanToInt("MCMXCIV") # 1994