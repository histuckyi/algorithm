"""
LeetCode 66. Plus One (Easy)
blog : https://daimhada.tistory.com/126
problem : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def plusOne(self, digits):
        """
        Runtime : faster than 61.90% of Python3
        Memory Usage : less than 5.29% of Python3
        """
        digits = list(map(str, digits))
        nums = int(''.join(digits))
        nums += 1
        nums = list(str(nums))
        return list(map(int, nums))

s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([4,3,2,1]))