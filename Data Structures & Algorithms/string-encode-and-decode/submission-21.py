class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str=""
        for str1 in strs:
            length=len(str1)
            new_str=str(length)+"#"+str1
            final_str+=new_str
        return final_str

    def decode(self, s: str) -> List[str]:
        og_strs=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            len_num=int(s[i:j])
            str1=s[j+1:j+len_num+1]
            og_strs.append(str1)
            i=j+1+len_num
        return og_strs



