class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        heap = []
        for i in score:
            heap.append(-1*i)
        
        heapq.heapify(heap)
        print(heap)

        table = {}
        idx = 1
        while len(heap) > 0:
            val = heappop(heap)
            table[-1*val] = idx
            idx += 1

        print(table)

        result = []
        for s in score:
            idx = table[s]
            print(f"{s}: {idx}")
            if idx == 1:
                result.append("Gold Medal")
            elif idx == 2:
                result.append("Silver Medal")
            elif idx == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(idx))
            #print(f"{val}:{idx}")

        return result
