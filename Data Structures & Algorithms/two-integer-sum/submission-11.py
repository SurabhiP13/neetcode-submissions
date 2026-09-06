class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A=[]
        for i in range(len(nums)):
            A.append([nums[i], i])
        A.sort()

        res=[]
        i,j=0, len(A)-1
        while i<j:
            if A[i][0]+A[j][0]==target:
                res.append(A[i][1])
                res.append(A[j][1])
                return sorted(res)
            elif A[i][0]+A[j][0]<target:
                i+=1
            else:
                j-=1

   




            
        