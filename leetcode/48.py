"""
LeetCode 48. Rotate Image
blog : https://daimhada.tistory.com/149
problem : https://leetcode.com/problems/rotate-image/
"""
import copy
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp_maxtrix = copy.deepcopy(matrix)

        n = len(matrix[0])
        for c in range(n):
            for r in range(n-1, -1, -1):
                last_index = n - 1
                matrix[c][abs(r - last_index)] = temp_maxtrix[r][c]



if __name__ == "__main__":
    s = Solution()
    test = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(test)