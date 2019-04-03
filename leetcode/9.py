"""
LeetCode 9. Palindrome Number
blog : https://daimhada.tistory.com/124
problem : https://leetcode.com/problems/palindrome-number
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        length = len(number)
        is_even = False

        # 길이가 0
        if length == 0:
            return True

        # 음수
        if x < 0:
            return False

        # 짝수 여부
        if length % 2 == 0:
            is_even = True

        # 중간 index
        mid = length // 2

        # x의 길이가 짝수 일 경우만 양쪽을 확인
        last_index = length - 1
        for i in range(mid, length):
            if not is_even:
                is_even = True
                continue

            opposition = last_index - i
            if number[opposition] != number[i]:
                return False
        return True


s = Solution()
print(s.isPalindrome(-121)) # False
print(s.isPalindrome(121)) # True
print(s.isPalindrome(10)) # False
print(s.isPalindrome(0)) # True
print(s.isPalindrome(100)) # False
