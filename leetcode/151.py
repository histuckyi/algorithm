"""
LeetCode 151. Reverse Words in a String (Medium)
blog : https://daimhada.tistory.com/150
problem: https://leetcode.com/problems/reverse-words-in-a-string/
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Runtime : faster than 100.00% of Python3
        Memory Usage : less than 100.00% of Python3
        """
        test = s.strip().split(' ')
        test.reverse()
        test = [item for item in test if item != '']
        return ' '.join(test)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("a good   example"))