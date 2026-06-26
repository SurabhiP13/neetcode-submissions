class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<=0:
            return False
        for i in range(len(nums)):
            if i==(len(nums)-1):
                return False
            for j in range(len(nums)):
                if i==j:
                    continue
                elif nums[i]==nums[j]:
                    return True


        