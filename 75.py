class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = Counter(nums)
        
        idx = 0
        for i in range(3):
            for k in range(freq[i]):
                nums[idx] = i
                idx += 1

        