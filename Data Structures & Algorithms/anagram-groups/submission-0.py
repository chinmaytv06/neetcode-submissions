class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        d = dict()
        for i in s:
            temp = i
            temp = list(temp)
            temp.sort()
            temp = str(temp)

            if temp in d.keys():
                d[temp].append(i)
            else:
                d[temp] = []
                d[temp].append(i)
            
        ans = []
        for i in d.values():
            ans.append(i)
        return ans
        