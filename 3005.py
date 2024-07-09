class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        heap = []

        for i in freq.values():
            heappush(heap,-i)

        biggest = -heappop(heap)
        total = biggest
        while len(heap) > 0:
            cur = -heappop(heap)
            if cur == biggest:
                total += cur
            else:
                break

        return total