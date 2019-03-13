# 완전 탐색
class Solution1:
    def maxSubArray(self, nums):
        mx = max(nums)
        for i in range(len(nums)):
            prev = nums[i]
            for j in range(i+1,len(nums)):
                prev += nums[j]
                if mx < prev:
                    mx = prev
        return mx

# 메모아이제이션 공감복잡도 n
class Solution2:
    def maxSubArray(self, nums):
        mem = [nums[0]]

        for i in range(1, len(nums)):
            mem.append(max(mem[-1] + nums[i], nums[i]))

        return max(mem)


class Solution3:
    def maxSubArray(self, nums):
        maxVal = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
            if maxVal < nums[i]:
                maxVal = nums[i]
        return maxVal

solution = Solution3()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))