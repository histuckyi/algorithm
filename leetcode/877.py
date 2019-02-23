"""
877. Stone Game
blog : https://daimhada.tistory.com/69
problem: https://leetcode.com/problems/stone-game/
"""
from functools import lru_cache

class Solution:
    def stoneGame(selfself, piles):
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            if i > j : return 0
            # Alex's turns if remain array element count is even
            parity = (j - N + 1) % 2
            if parity == 0: # Alex
                return max(piles[i] + dp(i+1, j), piles[j] + dp(i, j-1))
            else:
                return min(-piles[i] + dp(i+1, j) , -piles[j] + dp(i, j-1))
        return dp(0, N-1) > 0

game = Solution()
print(game.stoneGame([5,3,4,5]))