class Solution:    
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for str1 in strs:
            for c in str1:
                if c == ',' or c == '\\':
                    encoded.append("\\")
                encoded.append(c)
            encoded.append(',')

        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        result = []
        temp = []
        i = 0
        while i < len(s):
            if s[i] == ',' and i != len(s) - 1:
                result.append("".join(temp))
                temp = []
            elif s[i] == ',' and i == len(s) - 1:
                break
            else:
                if s[i] == '\\':
                    if i + 1 != len(s) and (s[i + 1] == ',' or s[i + 1] == '\\'):
                        i += 1
                temp.append(s[i])
            i += 1
        result.append("".join(temp))
        return result