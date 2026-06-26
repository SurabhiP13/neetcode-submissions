class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1={}
        for num in nums:
            hash1[num]=1+hash1.get(num, 0)
        ls=[]
        for num in hash1.keys():
            ls.append([hash1[num],num ])
        ls.sort()
        
        res=[]
        while len(res)<k:
            res.append(ls.pop()[1])
        return res
            


            
        