"""
1314. Matrix Block Sum
problem: https://leetcode.com/problems/matrix-block-sum/
"""


class Solution:

    @staticmethod
    def matrixBlockSum(mat, k):
        result_matrix = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                value = 0

                # r 범위 정하기
                r_start = 0 if i - k <= 0 else i - k
                r_end = len(mat) if len(mat) <= i + k else i + k + 1

                # c 범위 정하기
                c_start = 0 if j - k <= 0 else j - k
                c_end = len(mat[0]) if len(mat[0]) <= j + k else j + k + 1

                for r in range(r_start, r_end):
                    value += sum(mat[r][c_start:c_end])
                result_matrix[i][j] = value
        return result_matrix


if __name__ == "__main__":
    s = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # [[12,21,16],[27,45,33],[24,39,28]]
    k =1

    mat = [[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]]
    # [[731,731,731],[930,930,930],[930,930,930],[930,930,930],[721,721,721]]
    k = 3
    print(s.matrixBlockSum(mat, k))