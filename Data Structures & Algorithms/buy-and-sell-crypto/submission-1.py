class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_profit=float('-inf')
        if not prices:
            return 0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            profit=prices[i]-min_price
            if profit>max_profit:
                max_profit=profit

        return max_profit

