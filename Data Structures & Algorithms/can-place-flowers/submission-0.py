        
class Solution:
    def canPlaceFlowers(self, a: list[int], n: int) -> bool:

        if n == 0:
            return True

        if len(a) == 1 and a[0] == 1 and n > 0:
            return False

        if len(a) == 1 and a[0] == 0 and n == 1:
            return True

        if len(a) == 1 and a[0] == 0 and n > 1:
            return False

        for i in range(len(a)):
            if n == 0:
                return True

            if i == 0 and a[0] == 0 and a[1] == 0 and n > 0:
                a[0] = 1
                n -= 1

            elif (i == len(a) - 1 and a[i] == 0
                  and a[i - 1] == 0 and n > 0):
                a[i] = 1
                n -= 1

            elif (i + 1 < len(a) and i - 1 >= 0 and a[i - 1] == 0 and a[i] == 0 and a[i + 1] == 0 and n > 0):
                a[i] = 1
                n -= 1

        return n == 0  