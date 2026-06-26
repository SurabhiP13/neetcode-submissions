class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=+1000000000000
        max_price=-1000000000000
        profit=0
        # if len(prices)==0:
        #     return profit
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
                max_price=prices[i]
            if prices[i]>max_price:
                max_price=prices[i]
            curr_profit=max_price-min_price
            if curr_profit>profit:
                profit=curr_profit

        return profit



        