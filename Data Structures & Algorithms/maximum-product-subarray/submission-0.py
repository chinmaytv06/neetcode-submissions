class Solution:
    def maxProduct(self, n: list[int]) -> int:
        if not n:
            return 0

        d_max = [0]*len(n)
        d_min = [0]*len(n)
        d_max[0] = n[0]
        d_min[0] = n[0]

        for i in range(1,len(n)):
            d_max[i] = max(n[i] , n[i]*d_max[i-1] , n[i]*d_min[i-1] )
            d_min[i] = min(n[i] , n[i]*d_max[i-1], n[i]*d_min[i-1] )
            
            
        return max(d_max)
        