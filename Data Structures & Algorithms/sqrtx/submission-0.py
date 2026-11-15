class Solution:
    def mySqrt(self, x: int) -> int:
    
        n = 1
        while n*n < x:
            n += 1
        if n*n > x:
            return n-1
        else:
            return n
        