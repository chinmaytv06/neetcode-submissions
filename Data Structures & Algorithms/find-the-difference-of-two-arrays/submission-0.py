class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        a= set()
        b =set()
        for i in nums1:
            if i not in nums2:
                a.add(i)
        for j in nums2:
            if j not in nums1:
                b.add(j)
        # a = nums1.difference(nums2)
        # b = nums2.diffrence(nums1)
        return [list(a),list(b)]