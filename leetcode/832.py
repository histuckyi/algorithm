"""
LeetCode 832. Flipping an Image (Easy)
blog : https://daimhada.tistory.com/146
problem : https://leetcode.com/problems/flipping-an-image/
"""
class Solution:
    def flipAndInvertImage(self, A):
        for item in A:
            item.reverse()

            for i in range(len(item)):
                if item[i]:
                    item[i] = 0
                else:
                    item[i] = 1
        print(A)
        return A


if __name__ == "__main__":
    s = Solution()
    s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
    s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])

