class Solution:
    def getSum(self, a: int, b: int) -> int:
        # # if a < 1 and b <= 1:
        # #     return 0
        # x = []


        # for i in range(0,a):
        #     x.append(i)
            
        # for j in range(0,b):
        #     x.append(j)
        # return len(x)      


        # x=[0]*a
        # y=[0]*b
        # if a<0 or b<0:
        #     return 0
        
        # for i in y:
        #     x.append(i)
        # return len(x)

        return sum([a,b])
        