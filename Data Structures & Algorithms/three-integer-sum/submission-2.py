class Solution:
    def threeSum(self, n: list[int]) -> list[list[int]]:
        n.sort()
        ans =[]
        for i in range(len(n) - 2):

            # Skip duplicate first elements
            if i > 0 and n[i] == n[i - 1]:
                continue

            # All remaining numbers are non-negative
            if n[i] > 0:
                break

            j = i + 1
            k = len(n) - 1
            while(j<k):
                l = []
                x =(n[i] + n[j] + n[k])
                
                if x == 0:
                    l.append(n[i])
                    l.append(n[j])
                    l.append(n[k])
                    if l not in ans:
                        ans.append(l)
                    j+=1
                    k-=1
                elif x < 0:
                    j+=1
                else:
                    k-=1
            
        return ans