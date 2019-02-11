"""
LeetCode 33. Search in Rotated Sorted Array
blog : https://daimhada.tistory.com/50
problem : https://leetcode.com/problems/search-in-rotated-sorted-array/

# O(1)
def search(nums, target):
    try:
        return nums.index(target)
    except:
        return -1
"""

def search(nums, target):
    length = len(nums)
    if length < 1:
        return -1
    return bst(0, length - 1, nums, target)


def bst(s_index, e_index, nums, target):
    mid_index = (s_index + e_index) // 2
    mid_value = nums[mid_index]

    if s_index > e_index:
        return -1

    if target == mid_value:
        return mid_index

    start_value = nums[s_index]
    start_index = s_index
    end_index = e_index

    # this section([4,5,6]) in ascending order ex) 4,5,6,(7) 0 1 2  target : 5
    if start_value <= mid_value:
        if start_value <= target and target < mid_value:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    else:
    # This part([6,7,0]) is not sorted in ascending order. ex) 6,7,0,(1), 2, 3, 4, 5  target : 0
    # Check the opposite side.
        if mid_value < target and target <= nums[e_index]:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    return bst(start_index, end_index, nums, target)



print(search([4,5,6,7,0,1,2], 0)) # 4
print(search([4,5,6,7,0,1,2], 3)) # -1
print(search([], 5)) # -1
print(search([3,1], 0)) # -1
print(search([5,1,2,3,4],1))  # 1



