"""
LeetCode. 917. Reverse Only Letters
blog : https://daimhada.tistory.com/147
problem : https://leetcode.com/problems/reverse-only-letters/
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        """
        Runtime : faster than 92.02% of Python3
        Memory Usage : less than 5.56% of Python3
        """
        start_index = 0
        last_index = (len(S) - 1)

        if len(S) <= 1:
            return S

        S = list(S)
        while start_index < last_index:

            sv = S[start_index]
            lv = S[last_index]

            if not lv.isalpha():
                last_index -= 1
                continue

            if not sv.isalpha():
                start_index += 1
                continue

            S[start_index], S[last_index] = S[last_index], S[start_index]
            start_index += 1
            last_index -= 1

        return ''.join(S)


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = []
        for s in S:
            if s.isalpha():
                stack.append(s)
        result = ''
        for s in S:
            if s.isalpha():
                result += stack.pop()
            else:
                result += s
        return result



if __name__ == "__main__":
    s = Solution()
    print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
    print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"