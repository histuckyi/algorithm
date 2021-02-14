import copy

"""
LeetCode 1675.  Minimize Deviation in Array
priblem : https://leetcode.com/problems/minimize-deviation-in-array/
"""


class Solution:
    def minimumDeviation(self, nums):

        changed = True
        numSet = set(nums)
        nums = list(numSet)
        if len(nums) < 2:
            return 0
        nums.sort()

        while changed != False:
            if len(nums) < 2:
                return 0
            changed = False
            # 최댓값
            # 최댓값이 짝수일 경우
            if nums[-1] % 2 == 0:
                halfValue = nums[-1] // 2
                if halfValue >= nums[0]:
                    if halfValue in nums:
                        nums.pop()
                    else:
                        nums[-1] = halfValue
                        # 재정렬
                        nums.sort()
                        changed = True

            # 최솟값이 홀수 일 경우
            if nums[0] % 2 != 0:
                multiValue = nums[0] * 2
                if multiValue <= nums[-1]:
                    if multiValue in nums:
                        nums.pop(0)
                    else:
                        nums[0] = multiValue
                        nums.sort()
                        changed = True

            # 더이상 변경할 수 없다고 생각될 때
            if changed == False:
                # 최대값이 홀수이고 최소값이 홀수일 때 최솟값 * 2의 abs 값 체크
                if nums[0] % 2 != 0:
                    tempNums = copy.deepcopy(nums)
                    for idx in range(0, len(nums)):
                        if nums[idx] % 2 != 0:
                            multiValue = nums[idx] * 2
                            checkedValueAbs = abs(multiValue - nums[idx + 1])
                            if checkedValueAbs < abs(nums[-1] - nums[0]):
                                tempNums[idx] = multiValue
                                changed = True
                                break
                            tempNums[idx] = multiValue
                        else:
                            break

                if changed:
                    nums = tempNums
                    nums.sort()

            if changed == False:
                # 최대값이 짝수이고 최대값의 //2  값이 현재의 최소값보다 더 작아졌을 경우에 대한 경우의 수 체크
                changedIndex = []
                if nums[-1] % 2 == 0:
                    tempNums = copy.deepcopy(nums)
                    for idx in range(len(nums) -1, 0, -1):
                        # 뒤에서부터 짝수인 경우까지 계산할 것
                        if nums[idx] % 2 == 0:
                            halfValue = nums[idx] // 2
                            if 1 < halfValue:
                                checkedValueAbs = abs(nums[idx - 1] - halfValue)
                                if checkedValueAbs < abs(nums[-1] - nums[0]):
                                    tempNums[idx] = halfValue
                                    changed = True
                                    break
                                tempNums[idx] = halfValue
                            else:
                                break
                        else:
                            break
                    # 바꿔줘야하는 값들이 존재함
                    if changed:
                        nums = tempNums
                        nums.sort()

        return nums[-1] - nums[0]

if __name__ == "__main__":
    nums = [101977678,160897452,192978346, 136108503]  # result : 55659777
    nums = [195316256,122308978,164716217,117471904,194267446]  # 67582494
    nums = [195316256,165570519,161630895,174858873,138042671,122308978,164716217,117471904,155970321,136108503,194267446]   # 77725150
    # nums = [399,908,648,357,693,502,331,649,596,698] # 315
    # nums = [900,241,842,374,758,39,687,242,912]  # 609
    # nums = [203,538,789] # 383
    # nums = [3,5]
    s = Solution()
    print(s.minimumDeviation(nums))