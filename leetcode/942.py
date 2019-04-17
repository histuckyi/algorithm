"""
LeetCode 942. DI String Match (Easy)
blog : https://daimhada.tistory.com/139
problem : https://leetcode.com/problems/di-string-match/
"""

class Solution:
    def diStringMatch(self, S: str):
        """
        Runtime : faster than 72.85% of Python3
        Memory Usage : less than 5.62% of Python3
        """

        min_v = 0
        max_v = len(S)
        result_s = []

        for i in range(len(S)):
            if S[i] == "I":
                result_s.append(min_v)
                min_v += 1
            else:
                result_s.append(max_v)
                max_v -= 1

        result_s.append(min_v)
        return result_s


if __name__ == "__main__":
    s = Solution()
    s.diStringMatch("")
    s.diStringMatch("IDID")
    s.diStringMatch("III")
    s.diStringMatch("DDI")