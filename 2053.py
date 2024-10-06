class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        f = Counter(arr)
        
        count = 0
        for i in arr:
            if f[i] == 1:
                count+=1
                if count == k:
                    return i

        return ""