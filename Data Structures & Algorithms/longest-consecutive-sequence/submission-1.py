class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0

        for num in nums:
            streak=0
            curr=num
            while curr in nums:
                streak+=1
                curr+=1
            if streak>longest:
                longest=streak
        return longest






            



        

        