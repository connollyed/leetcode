class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        nums.sort()
        freq = Counter(nums)

        for i in nums:
            if freq[i] > 0:
                count = freq[i]

                for j in range(k):
                    if freq[i + j] < count:
                        return False
                    freq[i+j] -= count

        return True