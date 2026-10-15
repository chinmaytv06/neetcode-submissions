class Solution:
    def singleNumber(self, n: List[int]) -> int:
        d = {}
        for i in n:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j == 1:
                return i

        