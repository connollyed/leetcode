class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        biggest = -1
        prev = -1
        cur = -1

        i = len(arr) - 1
        while i >= 0:
            current = arr[i]
            biggest = max(biggest, prev)
            arr[i] = biggest
            prev = current
            i-=1

        return arr