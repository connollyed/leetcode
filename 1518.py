class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        filled = numBottles
        
        drink = 0
        empty = 0
        while filled > 0:
            drink += filled
            empty += filled

            filled = empty // numExchange
            empty = empty % numExchange
            #print(f"d={drink} e={empty} f={filled}")

        #print(f"d={drink} e={empty} f={filled}")
        return drink