class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d.keys() and d[s[i]] != t[i]:
                return False
            elif s[i] not in d.keys() and t[i] in d.values():
                return False
            else:
                d[s[i]] = t[i]
        

        
        return True