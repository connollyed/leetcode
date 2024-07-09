class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squared = [i**2 for i in nums]
        return sorted(squared)