class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        if len(prices)==0:
            return best
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                curr=prices[j]-prices[i]
                if curr>best:
                    best=curr
        return best

        