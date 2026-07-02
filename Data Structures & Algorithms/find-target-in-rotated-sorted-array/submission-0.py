class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hash1={}
        for i in range(len(nums)):
            hash1[nums[i]]=i
        if target in hash1:
            return hash1[target]
        else:
            return -1

        