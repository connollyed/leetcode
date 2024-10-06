class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        stack = [prices[0]] # lowest seen
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > stack[-1]:
                profit = max(profit, prices[i]-stack[-1])
            else:
                stack.append(prices[i])
        return profit