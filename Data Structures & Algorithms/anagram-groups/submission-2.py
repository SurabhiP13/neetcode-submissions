class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sortS=''.join(sorted(s)) 
            #this is required because otherwise its a list of sorted characters of the string
            res[sortS].append(s)
        return list(res.values())





        