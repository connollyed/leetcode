class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        #print(freq)

        freq_list = []
        for i,(value,frequency) in enumerate(freq.items()):
            #print(f"{value},{frequency}")
            
            if frequency not in freq_list:
                freq_list.append(frequency)
            else:
                return False

        return True