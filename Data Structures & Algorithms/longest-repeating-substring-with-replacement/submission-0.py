class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # freq={}
        # for i in range(len(s)):
        #     freq[s[i]]=1+freq.get(s[i], 0)
        maxlen=0
        for i in range(len(s)):
            freq, maxf={}, 0
            for j in range(i, len(s)):
                freq[s[j]]=1+freq.get(s[j], 0)
                maxf=max(maxf, freq[s[j]])
                rep=(j-i+1)-maxf
                if rep<=k:
                    maxlen=max(maxlen, j-i+1)
                else:
                    break

        return maxlen




            
 
        