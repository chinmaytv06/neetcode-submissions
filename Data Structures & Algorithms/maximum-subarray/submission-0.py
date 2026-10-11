class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        dp = [0]*len(n)
        dp[0] = n[0]
        for i in range(1,len(n)):
            dp[i] = max(dp[i-1]+n[i] ,n[i])
        return max(dp)
            


        