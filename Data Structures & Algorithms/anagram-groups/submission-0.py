class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs=[]
        for i in strs:
            sorted_strs.append(sorted(i))
        final_ls=[]
        
        for i in range(len(sorted_strs)):
            flag=False
            if len(final_ls)!=0:
                for ls in final_ls:
                    if sorted(ls[0])==sorted_strs[i]:
                        flag=True
            if flag==True:
                continue        
            if flag==False:
                group=[]
                group.append(strs[i])
            
                #if never encountered in final_ls then we append to the group
            for j in range(i+1, len(sorted_strs)):
                if sorted_strs[i]==sorted_strs[j]:
                    group.append(strs[j])
            final_ls.append(group)
        return final_ls

        