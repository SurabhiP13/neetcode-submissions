class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=i
        for i in range(len(nums)):
            check=target-nums[i]
            if check in hash_map and i!=hash_map[check]:
                return [i, hash_map[check]]


        

        