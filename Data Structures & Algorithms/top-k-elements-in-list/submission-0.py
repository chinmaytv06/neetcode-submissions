
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        ans = sorted(freq, key=freq.get, reverse=True)

        return ans[:k]