class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        z=""
        for i in range(len(s)-1,-1,-1):
            z+=s[i]
        if z != s:
            return False
        else:
            return True