class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        pal=0
        for i in range(n):
            for j in range(i, n):
                str1=s[i:j+1]
                str2=str1[::-1]
                if str1==str2:
                    pal+=1
        
        return pal

