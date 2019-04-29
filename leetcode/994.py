"""
LeetCode 994. Rotting Oranges (Easy)
blog : https://daimhada.tistory.com/161
problem : https://leetcode.com/problems/rotting-oranges/
"""

class Solution:
    def orangesRotting(self, grid) -> int:
        """
        Rumtime : faster than  84% of Python3
        Memory Usage : less tahn 5.12% of Python3
        """
        fresh_orange_count = 0
        rotten_orange_position = []
        next_rotten_orange_position = []
        changed = True
        time = 0
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        # 현재의 상자 정보 확인
        for i in range(len(grid)*len(grid[0])):
            r = i // len(grid[0])
            c = i % len(grid[0])
            v = grid[r][c]
            if v == 1:
                fresh_orange_count += 1
            elif v == 2:
                rotten_orange_position.append((r,c))


        # no fresh orange
        if fresh_orange_count == 0:
            return 0

        # no rotten orange
        if len(rotten_orange_position) == 0:
            return -1

        while changed:
            changed = False
            time += 1
            while rotten_orange_position:
                rotten_orange = rotten_orange_position.pop()
                r, c = rotten_orange
                for i in range(4):
                    temp_r = r + dr[i]
                    temp_c = c + dc[i]

                    if 0 <= temp_r < len(grid) and 0 <= temp_c < len(grid[0]):
                        # rot fresh orange
                        if grid[temp_r][temp_c] == 1:
                            grid[temp_r][temp_c] = 2
                            changed = True
                            fresh_orange_count -= 1

                            # All orange rottend
                            if fresh_orange_count == 0:
                                return time
                            next_rotten_orange_position.append((temp_r, temp_c))
            rotten_orange_position = next_rotten_orange_position
            next_rotten_orange_position = []

        if fresh_orange_count == 0:
            return time
        else:
            return -1


if __name__ == "__main__":
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(s.orangesRotting([[0,2]]))
