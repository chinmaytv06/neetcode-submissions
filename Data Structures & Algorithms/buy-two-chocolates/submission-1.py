class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        min_price = prices[0]+prices[1]
        if min_price > money:
            return money
        else:
            return abs(min_price - money)
        