class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        for i in n2:
            n1.append(i)
        n1.sort()

        if len(n1)%2 == 0:
            mid = len(n1)//2
            return (n1[mid]+n1[mid-1])/2
        elif len(n1)%2 != 0:
            mid = len(n1)//2
            return n1[mid]