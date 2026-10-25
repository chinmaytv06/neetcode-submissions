class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)

        for i in range(0,n+2):
            if i not in nums:
                return i
           
        