"""
LeetCode 7. Reverse Integer (Easy)
blog : https://daimhada.tistory.com/119
problem : https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:
        """
        Runtime : faster than 99.99% of Python3
        Memory Usage : less than 5.71% of Python3
        """
        if x == 0:
            return 0

        is_Negative = False
        if x < 0:
            is_Negative = True

        x = str(abs(x))
        i = 1
        result = 0
        # 321 -> 123 (3*1 + 2 * 10 + 1 * 100)
        for ch in x:
            result += (int(ch) * i)
            i *= 10

        if is_Negative:
            result *= -1

        max_size = pow(2, 31)
        if -max_size < result < max_size - 1:
            return result
        else:
            return 0


solution = Solution()
solution.reverse(123) # 321
solution.reverse(-123) # -321
solution.reverse(120) # 21