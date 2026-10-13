class Solution:
    def isValid(self, s: str) -> bool:
        a = []

        for i in s:
            if i == '(' or i == '[' or i == '{':
                a.append(i)
            elif len(a) != 0 and i == ')' and a[len(a)-1] =='(':
                a.pop()
            elif len(a) != 0 and i == '}' and a[len(a)-1] =='{':
                a.pop()
            elif len(a) != 0 and i == ']' and a[len(a)-1] =='[':
                a.pop()
            else:
                return False

        if len(a) == 0:
            return True
        else:
            return False