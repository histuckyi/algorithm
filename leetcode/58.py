"""
LeetCode. 58. Length of Last Word (Easy)
blog: https://daimhada.tistory.com/135
problem: https://leetcode.com/problems/length-of-last-word/

"""

# 방법 1 (split 사용하기)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Runtime : faster than 75.54% of Python3
        Memory Usage: less than 6.04% of Python3
        """
        return len(s.strip().split(' ')[-1])


# 방법 2 (reversed 사용하기)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Rumtime : faster than 75.54% of Python3
        Memory Usage : less than 6.04% of Python3
        """
        count = 0
        for c in reversed(s.strip()):
            if c == " ":
                break
            count += 1
        return count

# 방법 3 (최대 Index 사용하기)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Rumtime : faster than 75.54% of Python3
        Memory Usage : less than 6.04% of Python3
        """
        count = 0
        string = s.strip()
        for i in range(len(string)-1, -1, -1):
            if string[i] == " ":
                break
            count += 1

        return count


s = Solution()
print(s.lengthOfLastWord('hello world'))
print(s.lengthOfLastWord("a     "))
print(s.lengthOfLastWord(" "))
