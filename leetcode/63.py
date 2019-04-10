"""
LeetCode 63. Unique Paths II (Medium)
blog : https://daimhada.tistory.com/132
problem : https://leetcode.com/problems/unique-paths-ii/
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        """
        Rumtime : faster than 70.44% of Python3
        Memory Usage : less than 5.19% of Python3
        """
        direction = [(0,-1), (-1, 0)]
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(r):
            for j in range(c):
                # 맨 처음만 예외처리
                if i == 0 and j == 0:
                    obstacleGrid[0][0] = 1
                    continue

                # 장애물은 진입이 안되므로 0으로 처리
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue

                for next_pos in direction:
                    add_r, add_c = next_pos
                    temp_r = i + add_r
                    temp_c = j + add_c
                    if temp_r < 0 or temp_c < 0 or r <= temp_r or c <= temp_c:
                        continue
                    obstacleGrid[i][j] += obstacleGrid[temp_r][temp_c]
        print(obstacleGrid[r-1][c-1])
        return obstacleGrid[r-1][c-1]

s = Solution()

obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

obstacleGrid = [
  [0,0,1],
  [0,1,0],
  [1,0,0]
]

s.uniquePathsWithObstacles(obstacleGrid)