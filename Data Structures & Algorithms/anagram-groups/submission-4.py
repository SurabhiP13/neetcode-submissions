class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_strs={}
        for str1 in strs:
            sorted_i="".join(sorted(str1))
            if  sorted_i in sort_strs:
                sort_strs[sorted_i].append(str1)
            else:
                sort_strs[sorted_i]=[str1]

        res=[]
        for lis in sort_strs.values():
            res.append(lis)
        return res

