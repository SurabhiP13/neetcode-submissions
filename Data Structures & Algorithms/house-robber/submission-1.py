class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        t=[-1]* (n+1)
        t[0]=0
        t[1]=nums[0]

        for i in range(2, n+1):
            t[i]=max(t[i-2]+nums[i-1], t[i-1])
        res=0
        for i in range(n+1):
            res=max(res, t[i])

        return res

        