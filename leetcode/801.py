"""
LeetCode 801. Minimum Swaps To Make Sequences Increasing
priblem : https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
"""



def is_same_with_next_idx(cur_idx, arr):
    return arr[cur_idx] == arr[cur_idx + 1]

# 값이 증가하고 있는가
def is_increasing(cur_idx, arr):
    return arr[cur_idx] < arr[cur_idx + 1]


class Solution:

    def minSwap(self, A, B):
        last_idx = len(A) - 1
        cur_idx = 0
        count = 0
        while cur_idx < last_idx:
            if is_same_with_next_idx(cur_idx, A):
                count += 1
                A[cur_idx], B[cur_idx] = B[cur_idx], A[cur_idx]
                if cur_idx + 1 >= last_idx or is_same_with_next_idx(cur_idx + 1, B):
                    cur_idx += 3
                else:
                    cur_idx += 2
            elif is_same_with_next_idx(cur_idx, B):
                count += 1
                if cur_idx + 1 >= last_idx or is_same_with_next_idx(cur_idx + 1, A):
                    cur_idx += 3
                else:
                    cur_idx += 2
            elif not is_increasing(cur_idx, A) or not is_increasing(cur_idx, B):
                count += 1
                cur_idx += 2
            else:
                cur_idx += 1
        return count

if __name__ == "__main__":
    A = [1, 3, 5, 4]
    B = [1, 2, 3, 7] # 1

    # A = [0, 4, 4, 5, 9]
    # B = [0, 1, 6, 8, 10] # 1
    #
    # A = [0, 4, 4, 5, 9]
    # B = [0, 1, 6, 8, 10]  # 1

    #
    # A = [1, 3, 3, 5, 5, 7]
    # B = [1, 2, 4, 4, 6, 6]  # 2

    # A = [3, 3, 8, 9, 10]
    # B = [1, 7, 4, 6, 8]  # 1

    # A = [2, 3, 2, 5, 6]
    # B = [0, 1, 4, 4, 5]  # 1

    A = [0, 7, 8, 10, 10, 11, 12, 13, 19, 18]
    B = [4, 4, 5, 7, 11, 14, 15, 16, 17, 20] # 4

    s = Solution()
    print(s.minSwap(A, B))