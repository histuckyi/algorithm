"""
LeetCode 26. Remove Duplicates from Sorted Array
blog : https://daimhada.tistory.com/126
problem : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        Runtime : faster than 39.84% of Python3
        Memory Usage : less than 5.43% of Python3
        """
        temp = list(set(nums))
        temp.sort()
        for i, v in enumerate(temp):
            nums[i] = v
        return len(temp)


class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        Runtime : fater than 79.66% of Python3
        Memory Usage : less than 5.43% of Python3

        """
        if len(nums) == 0:
            return 0
        change_index = 1
        for i in range(0, len(nums)):
            if i != 0 and nums[i - 1] != nums[i]:
                nums[change_index] = nums[i]
                change_index += 1
        print(change_index)
        return change_index


s = Solution()
s.removeDuplicates([0,1,1,2,3,4,4,4,4,4,5,6,7,8,9,11])  # 11
s.removeDuplicates([0,1,2,3,4,5]) # 6
s.removeDuplicates([-1]) # 1
