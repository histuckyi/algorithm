"""
LeetCode 27. Remove Element
blog : https://daimhada.tistory.com/127
problem : https://leetcode.com/problems/remove-element/
"""

class Solution:
    def removeElement(self, nums, val) -> int:
        """
        Runtime: faster than 99.16% of Python3
        Memory Usage : faster than 5.09% of Python3
        """
        idx = 0
        while nums.count(val):
            nums.remove(val)
        print(nums)
        return len(nums)


s = Solution()
s.removeElement([0,1,2,2,3,0,4,2], 2) # [0,1,4,0,3]
s.removeElement([3, 2, 2, 3], 3) # []


