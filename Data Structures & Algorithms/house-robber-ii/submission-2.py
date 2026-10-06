class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[n-1]
        x=self.solve(nums[:-1])
        y=self.solve(nums[1:])

        return max(x, y)


    def solve(self, nums):
        n=len(nums)
        t=[-1]*(n+1)
        t[0]=0
        t[1]=nums[0]
        for i in range(2, n+1):
            t[i]=max(
                t[i-2]+ nums[i-1],
                t[i-1]
            )
        return t[n]








        