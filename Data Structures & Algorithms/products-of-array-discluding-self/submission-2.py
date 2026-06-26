class Solution:

    def prefix_sum(self,nums: List[int])->List[int]:
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        return res
    
    def suffix_sum(self,nums: List[int])-> List[int]:
        res=[1]*len(nums)
        suffix=1
        for i in range(len(nums)-1, -1, -1):
            # idx=len(nums)-i
            res[i]=suffix
            suffix*=nums[i]
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod=self.prefix_sum(nums)
        suffix_prod=self.suffix_sum(nums)

        prod=[1]*len(nums)

        for i in range(len(nums)):
            prod[i]=suffix_prod[i]*prefix_prod[i]

        return prod


        
        


        