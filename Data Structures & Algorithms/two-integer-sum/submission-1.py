class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        for i in range(len(n)):
            for j in range(1,len(n)):
                if n[i] + n[j] == t and i!=j:
                    return [i,j]
                