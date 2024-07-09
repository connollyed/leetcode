class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        max_heap = [-h for h in happiness]
        heapq.heapify(max_heap)

        total = 0
        turn = 0
        for i in range(k):
            total += max(-heapq.heappop(max_heap) - turn, 0)
            
            turn+=1

        return total