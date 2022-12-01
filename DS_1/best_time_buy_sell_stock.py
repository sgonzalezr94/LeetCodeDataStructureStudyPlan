# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan&id=data-structure-i

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = min_idx = 0
        min = prices[0]
        profit = 0
        while i < len(prices):
            if prices[i] < min:
                min = prices[i]
                min_idx = i
            if prices[i] - prices[min_idx] > profit:
                profit = prices[i] - prices[min_idx]
            i += 1
        return profit


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
sol.maxProfit(prices)

#  1088 ms, faster than 91.78% of Python3 online submissions for Best Time to Buy and Sell Stock.
