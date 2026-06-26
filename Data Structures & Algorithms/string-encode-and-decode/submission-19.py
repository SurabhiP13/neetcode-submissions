class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for str1 in strs:
            encoded.append(str(len(str1)))
            encoded.append("#")
            encoded.append(str1)
        return "".join(encoded)



    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < (len(s)):
            j=i
            while s[j]!="#":
                j+=1
            len_s=int(s[i:j])
            str1=""
            str1=s[j+1:j+1+len_s]
            i=j+1+len_s
            res.append(str1)
            
        return res
        
                


        

            
