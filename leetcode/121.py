"""
121. Best Time to Buy and Sell Stock
blog : https://daimhada.tistory.com/100
problem : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
import heapq

class Solution1(object):
    def maxProfit(prices):
        """
        Time    O(nlogn)
        Space   O(n) heap
        8 ms, faster than 34.66%
        """
        if len(prices) < 2:
            return 0
        pq = []
        diff = 0
        for price in prices:
            heapq.heappush(pq, price)
            if price - pq[0] > diff:
                diff = price - pq[0]
        print(diff)
        return diff

class Solution2(object):
    def maxProfit(prices):
        last_idx = len(prices) -1
        max_profit = 0
        max_index = -1
        max_v = -1
        for idx, p in enumerate(prices):

            if idx < last_idx and p > prices[idx + 1]:
                continue

            # 새로운 최대값을 찾는다
            if max_index <= idx:
                temp = prices[idx+1:]
                if temp:
                    max_v = max(temp)
                    max_index = (idx + 1) + temp.index(max_v)
                else:
                    max_v = -1
                    max_index = -1

            if p < max_v:
               profit = max_v - p
               if max_profit < profit:
                max_profit = max_v - p
        print(max_profit)
        return max_profit


if __name__ == "__main__":
    Solution2.maxProfit([7,1,5,3,6,4]) # 5
    Solution2.maxProfit([7,6,4,3,1]) # 0
    Solution2.maxProfit([9,2,3,8,1,5]) # 6
    Solution2.maxProfit([2,4,1]) # 2
    Solution2.maxProfit([])

    Solution1.maxProfit([7,1,5,3,6,4]) #5
    Solution1.maxProfit([7,6,4,3,1]) # 0
    Solution1.maxProfit([9,2,3,8,1,5]) # 6
    Solution1.maxProfit([2,4,1]) # 2