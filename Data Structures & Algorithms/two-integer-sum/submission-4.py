class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        
        seen = {}        
        for i in range(len(n)):
            x = t - n[i]
            if x in seen:
                return [seen[x],i]
            else:
                seen[n[i]] = i
       
