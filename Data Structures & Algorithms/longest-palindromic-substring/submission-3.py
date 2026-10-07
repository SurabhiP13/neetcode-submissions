class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        a=s
        b=s[::-1]
        rows, cols=n+1, n+1
        t=[[-1]*cols for _ in range(rows)]
        
        for i in range(n+1):
            for j in range(n+1):
                if i==0 or j==0:
                    t[i][j]=""
        res=""
        for i in range(1, n+1):
            for j in range(1, n+1):
                if a[i-1]==b[j-1]:
                    t[i][j]=t[i-1][j-1]+ a[i-1]
                    check=t[i][j]
                    if len(t[i][j])>len(res) and (check==check[::-1]) :
                        res=t[i][j]

                else:
                    t[i][j]=""

        return res

        