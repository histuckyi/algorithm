"""
LeetCode 67. Add Binary (Easy)
blog : https://daimhada.tistory.com/136
problem: https://leetcode.com/problems/add-binary/

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Runtime : faster than 94.74% of Python3
        Memory Usage : less than 5.43% of Python3
        """
        return format(int(a, 2) + int(b, 2),'b')


s = Solution()
s.addBinary("11", "1")
s.addBinary("1010", "1011")

""""
이진법의 문자열을 십진법으로 바꾸는 방법

int("1010", 2)  # 10
int("0110", 2)  # 6


십진법의 수를 이진법으로 바꾸는 방법

format(3, 'b')  # '11'
format(6, 'b')  # '110"

"""
