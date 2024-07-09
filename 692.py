class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq_map = Counter(words)
#        print(freq_map)

        heap = []
        for key,val in freq_map.items():
#            print(f"{k}:{v}")
            heappush(heap, (-val,key))

        #print(heap)

        res = []
        for i in range(k):
            val,key = heappop(heap)
            res.append(key)

        return res

        