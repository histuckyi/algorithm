"""
LeetCode 1. Two Sum
blog : https://daimhada.tistory.com/55
problem : https://leetcode.com/problems/two-sum/
"""

def twoSum(nums, target):
    sorted_nums = sorted(nums) # ascending order
    last_index = len(nums) - 1

    for i in range(0, last_index):
        current_v = sorted_nums[i]
        extra_v = target - current_v
        if extra_v in sorted_nums[i + 1:last_index + 1]:
            first_index = nums.index(current_v)
            second_index = nums.index(extra_v)
            if first_index == second_index:
                second_index = (first_index + 1) + nums[first_index+1:].index(extra_v)
            print([first_index, second_index])
            return [first_index, second_index]

twoSum([2,7,11,15], 9) #[0,1]
twoSum([3,2,4], 6) # [1,2]
twoSum([3,3], 6) # [0,1]
twoSum([0,4,3,0], 0) # [0,3]
twoSum([-3,4,3,90], 0) # [0,2]



