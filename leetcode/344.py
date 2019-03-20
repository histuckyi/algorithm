"""
LeetCode 344. Reverse String
blog : https://daimhada.tistory.com/98
problem : https://leetcode.com/problems/reverse-string/
"""

class Solution1:
    def reverseString(self, s: List[str]) -> None:
        def helper(s: List[str], i: int, j: int) -> None:
            if i >= j:
                return
            s[i], s[j] = s[j], s[i]
            helper(s, i + 1, j - 1)

        helper(s, 0, len(s) - 1)


class Solution2:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lists = list(s)
        rev_list = lists[::-1]
        return ''.join(rev_list)