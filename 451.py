class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = [0] * 128

        for i in s:
            freqs[ord(i)] += 1

        heap = []
        for idx,val in enumerate(freqs):
            if val > 0:
                heapq.heappush(heap, (-1 * val, chr(idx)))

        
        ret_str = ""
        while heap:
            count, letter = heapq.heappop(heap)
            ret_str += (letter * -count)

        #print(ret_str)
        return ret_str
    
