"""
LeetCode 268. Missing Number
blog : https://daimhada.tistory.com/159
problem : https://leetcode.com/problems/missing-number/
"""

class Solution:
    def missingNumber(self, nums) -> int:
        """
        Runtime : faster than 33.94% of Python3
        Memory Usage : less than 5.25% of Python3
        """
        max_v = 0
        total = 0
        isinZero = False

        for n in nums:
            if n == 0:
                isinZero = True
            total += n
            max_v = max(max_v, n)

        if not isinZero:
            return 0

        result = int(max_v*(max_v + 1)/2 - total)

        if result == 0:
            return max_v + 1

        return result


s = Solution()
print(s.missingNumber([3,0,1])) # 2
print(s.missingNumber([0, 1]))  # 2
print(s.missingNumber([0]))  # 1
print(s.missingNumber([1]))  # 0
print(s.missingNumber([9,6,4,2,3,5,7,0,1])) # 8