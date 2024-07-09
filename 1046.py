class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        for i in stones:
            heappush(heap, -i)

        print(heap)
        while len(heap) > 1:
            y = -heappop(heap)
            x = -heappop(heap)
            
            if x != y:
                # x destroyed, y = y - x
                y = y-x
                heappush(heap,-y)


        return -heappop(heap) if len(heap)==1 else 0
        