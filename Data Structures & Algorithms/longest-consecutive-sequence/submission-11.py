class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dict1={}
        for i in range(len(nums)):
            dict1[nums[i]]=1+dict1.get(nums[i], 0)

        best=1

        for num in dict1:
            longest=1
            if num-1 not in dict1:
                
                while num+1 in dict1:
                    longest+=1
                    num+=1
            best=max(best, longest)

        return best

        

        
            
        
        