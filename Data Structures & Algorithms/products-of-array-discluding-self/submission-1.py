class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:
        pre = [0]*len(n)
        suf = [0]*len(n)

        prod = 1
        for i in range(len(n)):
            prod *=n[i]
            pre[i] = prod
        
        prod = 1 
        for j in range(len(n)-1,-1,-1):
            prod *= n[j]
            suf[j] = prod

        
        if len(n)==2:
            n[0] = suf[1]
            n[1] = pre[0]

            return n

        n[0] = suf[1]
        n[len(n)-1] = pre[len(n)-1-1]

        for i in range(1,len(n)-1):
            n[i] = pre[i-1]*suf[i+1]
        return n