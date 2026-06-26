class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums=set(nums)

        longest=1
        for num in nums:
            if num-1 in nums:
                continue
            streak=1
            curr=num
            while curr+1 in nums:
                streak+=1
                curr+=1
            longest=max(streak, longest)

        return longest






  










            



        

        