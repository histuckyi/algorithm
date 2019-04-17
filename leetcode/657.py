"""
LeetCode 657. Robot Return to Origin (Easy)
blog : https://daimhada.tistory.com/138
problem : https://leetcode.com/problems/robot-return-to-origin/
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:

        r, c = 0, 0
        length = len(moves)

        if length % 2 != 0:
            return False

        for i in range(length):
            ch = moves[i]

            if ch == "R":
                c += 1
            elif ch == "L":
                c -= 1
            elif ch == "U":
                r += 1
            elif ch == "D":
                r -= 1

        if r == 0 and c == 0:
            return True
        return False



if __name__ == "__main__":
    s = Solution()
    print(s.judgeCircle(""))
    print(s.judgeCircle("UD"))
    print(s.judgeCircle("LL"))
