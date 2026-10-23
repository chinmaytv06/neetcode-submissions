class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        x = 0
        for n in digits:
            x=x*10
            x = x+n
        z = x+1

        a = []
        while(z!=0):
            r = z%10
            z = z//10
            a.append(r)
        a.reverse()
        return a

            
