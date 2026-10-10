class Solution:
    def isHappy(self, n: int) -> bool:
        
        d = set()
        while (n!=1 and n not in d):
            d.add(n)
            sum = 0
            
            while(n > 0):
                r = n%10
                sum = sum +(r*r)
                n = n//10
                
            
            n = sum
        return n == 1