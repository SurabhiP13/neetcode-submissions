class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        rows, cols=n+1, amount+1

        t=[[-1] * cols for _ in range(rows)]
        for i in range(n+1):
            for j in range(amount+1):
                if i==0:
                    t[i][j]=float("inf")
                if j==0:
                    t[i][j]=0
        
        for j in range(1, amount+1):
            if j%coins[0]==0:
                t[1][j]=j/coins[0]
            else:
                t[1][j]=float("inf")
        for i in range(2, n+1):
            for j in range(1, amount+1):
                if coins[i-1]<=j:
                    t[i][j]=min(1+t[i][j-coins[i-1]],
                                t[i-1][j]
                    )
                else:
                    t[i][j]=t[i-1][j]
        if t[n][amount] == float("inf"):
            return -1

        return int(t[n][amount])

        


        

        