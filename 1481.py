class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        res = 0
        freq_map = Counter(arr)
        
        heap = []
        for i in freq_map.values():
            heappush(heap, i)

        #print(heap)

        while k > 0:
            if heap[0] <= k:
                k -= heappop(heap)
                #print(f"k={k}")
            else:
                break

        #print(heap)
        return len(heap)