class Solution:
    def searchInsert(self, n: List[int], t: int) -> int:
        i=0
        j=len(n)-1

        while(i<=j):
            mid = (i+j)//2

            if n[mid] == t:
                return mid 

            elif n[mid] < t:
                i = mid+1
            else:
                j =mid-1
        return i     