"""
LeetCode 189. Rotate Array (Easy)
blog : https://daimhada.tistory.com/113
problem : https://leetcode.com/problems/rotate-array
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        # if len(num) < k, it is equal k % len(num)
        n = k % len(nums)

        # front
        for i in range(0, n):
            if n - 1 - i < i or i == n - 1 - i:
                break
            nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]

        # back
        for i in range(n, len(nums)):
            if len(nums) - 1 - (i - n) < i or i == len(nums) - 1 - (i - n):
                break
            nums[i], nums[len(nums) - 1 - (i - n)] = nums[len(nums) - 1 - (i - n)], nums[i]

