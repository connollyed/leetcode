class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        freq_map = Counter(nums)
       
        for num,freq in freq_map.items():
            print(f"{num} : {freq}")
            heappush(heap, (-freq,num))

        res = []

        for i in range(0,k):
            freq, num = heappop(heap)
            res.append(num)

        return res