class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        if purchaseAmount % 10 != 0:
            rounded = (purchaseAmount + 5)// 10
            cost = rounded * 10
        else:
            cost = purchaseAmount 

        return 100 - cost
    

# IMPROVED VERSION
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        rounded = (purchaseAmount + 5)// 10
        cost = rounded * 10

        return 100 - cost
    

# COULD MAKE IT A 1 LINER