class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Using 2 dict"""
        if len(s) != len(t):
            return False

        d = {}
        d2 = {}
        for i in s:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        
        for j in t:
            if j not in d2.keys():
                d2[j]=1
            else:
                d2[j]+=1
        if d != d2:
            return False
        else:
            return True
        # for i in d.keys():
        #     if i not in  d2.keys():
        #         return False
        #     elif d[i] != d2[i]:
        #         return False
        # return True
        """Using one dict"""
        # if len(s) != len(t):
        #     return False

        # d = {}
       
        # for i in s:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # for i in t:
        #     if i in d:
        #         d[i]-=1
        #         if d[i]<0:
        #             return False
        #     else:
        #         return False
        # return True
           
                
        