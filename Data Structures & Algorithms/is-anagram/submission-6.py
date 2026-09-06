class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_t="".join(sorted(t))
        sort_s="".join(sorted(s))

        return sort_s==sort_t        