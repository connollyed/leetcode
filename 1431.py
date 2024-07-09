class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        biggest = max(candies)
        after_extra = [(i+extraCandies) >= biggest for i in candies]
        return after_extra