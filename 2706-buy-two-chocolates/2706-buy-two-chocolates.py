class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        


        if prices[0]+prices[1] <= money:
            if money-(prices[0] + prices[1])>=0:
                return money-(prices[0] + prices[1])
        else:
            return money

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n = len(prices)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if prices[i] > prices[j]:
                    prices[i], prices[j] = prices[j], prices[i]
        x = prices[0] + prices[1]

        if x <= money:
            return money - x
        else:
            return money
