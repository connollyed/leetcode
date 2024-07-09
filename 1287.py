class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        percent25 = n/100 * 25

        cur_count = 1
        cur_value = arr[0]
        for i in range(1,n):
            if cur_value == arr[i]:
                cur_count += 1
            else:
                cur_count = 1
                cur_value = arr[i]

            if cur_count > percent25:
                return cur_value
        
        return cur_value