class Solution:
    def search(self, n: List[int], t: int) -> int:
        # l = 0
        # r = len(n)-1
        # while(l<=r):
        #     if n[l] == t:
        #         return l
        #     elif n[r] == t:
        #         return r
        #     elif n[l] > l:
        #         l+=1
        #     else:
        #         r-=1
        # return -1

        for i in range(len(n)):
            if n[i] == t:
                return i
        return -1
