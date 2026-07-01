class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxlen=0, 0
        hash1={}
        maxf=0
        for r in range(len(s)):
            hash1[s[r]]=1+hash1.get(s[r], 0)
            maxf=max(maxf, hash1[s[r]])
            if r-l+1-maxf>k:
                hash1[s[l]]-=1
                l+=1
            if r-l+1-maxf<=k:
                maxlen=max(maxlen, r-l+1)
        return maxlen




            
 
        