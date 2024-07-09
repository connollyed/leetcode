class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        print(prices)


        spending_money = money
        purchases = 0
        for i in prices:
            if (spending_money - i) >= 0:
                spending_money -= i 
                purchases += 1

                if purchases == 2:
                    return spending_money
        
        return money