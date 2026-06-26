class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        best=0
        hash1={}
        
        for r in range(len(s)):
            if s[r] in hash1:
                l=max(hash1[s[r]]+1, l)
            hash1[s[r]]=r
            best=max(best, r-l+1)
        
        return best            






