class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        psum = 0
        submax = n[0]

        for i in n:
            psum = max(psum+i ,i)
            submax = max(submax,psum)
        return submax

        