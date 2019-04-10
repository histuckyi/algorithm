"""
LeetCode 62. Unique Paths
blog : https://daimhada.tistory.com/131
problem : https://leetcode.com/problems/unique-paths/submissions/
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r = n
        c = m
        field = [[0]*c for i in range(r)]
        rd = [0, 1]
        cd = [1, 0]
        pos_list = [(0,0)]
        while pos_list:
            pos = pos_list.pop()
            pr, pc = pos
            field[pr][pc] += 1
            for i in range(2):
                temp_r = pr + rd[i]
                temp_c = pc + cd[i]
                if temp_r < 0 or temp_c < 0 or r <= temp_r or c <= temp_c:
                    continue
                pos_list.append((temp_r, temp_c))
        return field[r-1][c-1]



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Runtime : faster than 40.64% of Python3
        Memory Usage : less than 5.25% of Python3
        """
        r = n
        c = m
        field = [[0]*(c) for i in range(r)]
        direction = [(0,-1), (-1, 0)]

        for i in range(r):
            for j in range(c):
                if i == 0 or j == 0:
                    field[i][j] = 1
                    continue

                for next_pos in direction:
                    add_r, add_c = next_pos
                    temp_r = i + add_r
                    temp_c = j + add_c
                    if temp_r < 0 or temp_c < 0 or r <= temp_r or c <= temp_c:
                        continue
                    field[i][j] += field[temp_r][temp_c]
        return field[r-1][c-1]


s = Solution()
s.uniquePaths(7,3)