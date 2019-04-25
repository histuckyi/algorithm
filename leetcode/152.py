"""
LeetCode 152. Maximum Product Subarray
blog : https://daimhada.tistory.com/151
problem : https://leetcode.com/problems/maximum-product-subarray/

"""
class Solution:
    def maxProduct(self, nums):
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum


from functools import reduce

class Solution:
    def maxProduct(self, nums):
        maximum = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                maximum = max(maximum, reduce(lambda x, y: x * y, nums[i:j+1]))
        return maximum

if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2,0,-1]))
    print(s.maxProduct([0]))
    print(s.maxProduct([-2]))
    print(s.maxProduct([0, 2]))
    print(s.maxProduct([-2,3, -4]))
