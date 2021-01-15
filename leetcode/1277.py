"""
LeetCode 1277. Count Square Submatrices with All Ones
problem : https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Runtime: 1116 ms, faster than 6.81% of Python3 online submissions for Count Square Submatrices with All Ones.
Memory Usage: 16.4 MB, less than 85.47% of Python3 online submissions for Count Square Submatrices with All Ones.
"""


class Solution:

    @staticmethod
    def countSquares(matrix):
        changed = True
        while changed:
            changed = False

            for x_idx in range(len(matrix)):
                for y_idx in range(len(matrix[0])):
                    current_count = matrix[x_idx][y_idx]
                    if current_count != 0:
                        around_list = [[0,1],[1, 1],[1, 0]]  # 아래, 대각선, 오른쪽
                        for add_x, add_y in around_list:
                            if 0 <= x_idx + add_x < len(matrix) and 0 <= y_idx + add_y < len(matrix[0]):
                                if matrix[x_idx + add_x][y_idx + add_y] != current_count:
                                    break
                            else:
                                break
                        else:
                            # break이 없었던 경우, 모두의 값이 같았을 경우
                            changed = True
                            matrix[x_idx][y_idx] += 1
        total = 0
        for row in matrix:
            total += sum(row)
        return total


if __name__ == "__main__":
    s = Solution()
    matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1] # 15
]
    # matrix = [[0,1,0,0,0],
    #           [0,0,0,0,1],
    #           [0,0,1,0,0]]  # 3

    # matrix = [[0,1,1,1],
    #           [1,1,1,1],
    #           [0,1,1,1]]  # 15
print(s.countSquares(matrix))

