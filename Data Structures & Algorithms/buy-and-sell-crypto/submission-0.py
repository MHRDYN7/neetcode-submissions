class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        best = 0


        for price in prices:
            mn = min(mn, price)
            best = max(best, price-mn)

        return max(best,0)

        