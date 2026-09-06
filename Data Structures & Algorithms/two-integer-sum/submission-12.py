class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        res=[]
        for i in range(len(nums)):
            # 
            check=target-nums[i]
            if check in dict1:
                res.append(i)
                res.append(dict1[check])
                return sorted(res)
            else:
                dict1[nums[i]]=i
                
        






            
        