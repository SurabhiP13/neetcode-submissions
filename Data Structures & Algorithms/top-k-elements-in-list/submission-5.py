class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1={}
        for num in nums:
            hash1[num]=1+hash1.get(num,0)

        heap=[]
        # heapify(heap)
        for num in hash1.keys():
            heapq.heappush(heap, (hash1[num], num))
            if len(heap)>k:
                heapq.heappop(heap)

        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res





            
        