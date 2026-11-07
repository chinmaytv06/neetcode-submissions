# class Solution:
#     def reverse(self, x: int) -> int:
#         a=0
#         while(x!=0):
#             r = x%10
#             x= x//10

#             a = a*10 
#             a=a+r
#         return a       

class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        x = abs(x)

        a = 0

        while x != 0:
            r = x % 10
            x = x // 10

            a = a * 10 + r

        a = a * sign

        if a < -(2**31) or a > (2**31 - 1):
            return 0

        return a