class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls=[]
        for i in range(len(nums)):
            ls.append([nums[i], i])

        ls.sort()
        i=0
        j=len(nums)-1
        while i<j:
            curr=ls[i][0]+ls[j][0]
            if curr==target:
                return [min(ls[i][1], ls[j][1]),
                        max(ls[i][1], ls[j][1])]
            elif ls[i][0]+ls[j][0]>target:
                j=j-1
            else:
                i=i+1
        return []

        

        