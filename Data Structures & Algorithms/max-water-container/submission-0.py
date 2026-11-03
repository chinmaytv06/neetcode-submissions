class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h)-1

        water = []

        while(l < r):
            curr = min(h[l],h[r])*(r-l)
            water.append(curr)
            if h[l] > h[r]:
                r-=1
            else:
                l+=1
            
        return max(water)
