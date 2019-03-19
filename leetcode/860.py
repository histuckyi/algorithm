"""
LeetCode 860. Lemonade Change
blog : https://daimhada.tistory.com/96
priblem : https://leetcode.com/problems/lemonade-change/
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5, bill10 = 0, 0

        for cur in bills:
            # current bill is not $5 and don't have $5 bill for change
            if cur != 5 and not bill5:
                return False

            if cur == 5:
                bill5 += 1
            elif cur == 10:
                bill5 -= 1
                bill10 += 1
            elif cur == 20:
                if 0 < bill10:
                    bill10 -= 1
                    bill5 -= 1
                elif bill5 > 3:
                    bill5 -= 3
                else:
                    return False
        return True

