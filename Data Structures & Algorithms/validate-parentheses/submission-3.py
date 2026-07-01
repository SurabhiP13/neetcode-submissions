class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        paran={
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i=='(' or i=="[" or i=="{":
                stack.append(i)
            else:
                if not stack:
                    return False
                last_open=stack.pop()
                if paran[i]!=last_open:
                    return False
        if not stack:
            return True
        else:
            return False
                       