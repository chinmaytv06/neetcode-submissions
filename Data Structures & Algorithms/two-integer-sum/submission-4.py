class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        # for i in range(len(n)):
        #     for j in range(1,len(n)):
        #         if n[i] + n[j] == t and i!=j:
    #             return [i,j]
        seen = {}
        
        
        for i in range(len(n)):
            x =t - n[i]
            if x in seen:
                return [seen[x],i]
            else:
                seen[n[i]] = i
       
