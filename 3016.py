class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        
        heap = []
        for k,v in freq.items():
            heappush(heap, (-v,k))

        count = 0
        total_presses = 0
        digit_set = 1
        while len(heap) > 0:
            v,k = heappop(heap)

            v = -v
            count += v * digit_set 
            total_presses += 1
            if total_presses % 8 == 0:
                digit_set += 1
            
        return count