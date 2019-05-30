"""
LeetCode 506. Relative Ranks
blog : https://daimhada.tistory.com/171
problem : https://leetcode.com/problems/relative-ranks/
"""


class Solution:
    def findRelativeRanks(self, nums):
        sorted_nums = sorted(nums, reverse=True)
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        # result = [0]*len(sorted_nums)
        i = -1
        for n in sorted_nums:
            i += 1
            idx = nums.index(n)
            if i < 3:
                nums[idx] = medal[i]
                continue
            nums[idx] = str(i + 1)
        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.findRelativeRanks([5, 4, 3, 2, 1]))
    print(s.findRelativeRanks([1, 2, 3, 4, 10])) # ['5', '4', "Bronze Medal", "Silver Medal", "Gold Medal"]
    print(s.findRelativeRanks([1, 2, 20, 4, 10])) # ['5', '4', 'Gold Medal', 'Bronze Medal', 'Silver Medal']
