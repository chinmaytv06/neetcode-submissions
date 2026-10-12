class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        low, high = 1, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            count = sum(1 for x in nums if x <= mid)
            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low