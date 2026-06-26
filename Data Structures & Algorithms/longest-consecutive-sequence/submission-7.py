class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        longest=1
        small=float('-inf')
        streak=1
        for i in range(len(nums)):
            if small==nums[i]-1:
                streak+=1
                small=nums[i]
            elif small==nums[i]:
                continue
            else:
                if streak>longest:
                    longest=streak
                streak=1
                small=nums[i]
        longest=max(streak, longest)
        return longest



  










            



        

        