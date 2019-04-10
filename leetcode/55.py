"""
LeetCode 55. Jump Game (Medium)
blog : https://daimhada.tistory.com/133
problem : https://leetcode.com/problems/jump-game/
"""

class Solution:
    def canJump(self, nums) -> bool:
        length = len(nums)

        avail_idx = 0
        for cur_i in range(length):
            # not accessible index
            if cur_i != 0 and avail_idx < cur_i:
                return False
            avail_last_index = cur_i + nums[cur_i]
            # If avail_last_index is greater than the avail_idx, replace avail_idx
            if avail_idx < avail_last_index:
                avail_idx = avail_last_index

            # available
            if (length -1) <= avail_last_index:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.canJump([0])) # True
    print(s.canJump([3,0,8,2,0,0,1])) # True
    print(s.canJump([2,3,0,0,0])) # True
    print(s.canJump([2,3,1,1,4])) # True
    print(s.canJump([3,2,1,0,4])) # False
