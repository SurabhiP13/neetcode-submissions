class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash1={}
        longest=0
        for num in nums:
            hash1[num]=1+hash1.get(num, 0)
        for i in range(len(nums)):
            streak=0
            curr=nums[i]
            if nums[i]-1 not in hash1:
                while curr in nums:
                    streak+=1
                    curr+=1
            if streak and streak>longest:
                longest=streak
        return longest










            



        

        