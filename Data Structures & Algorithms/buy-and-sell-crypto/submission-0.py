class Solution:
    def maxProfit(self, p: List[int]) -> int:
        maxprofit = 0 
        minPrice = p[0]
        lenth = len(p)
        for i in range(1,lenth):

            if p[i] < minPrice:
                minPrice = p[i]

            curr_profit = p[i] - minPrice
            if curr_profit > maxprofit:
                maxprofit = curr_profit
                
            
                
        return maxprofit

        