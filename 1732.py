class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        cur = 0
        max_altitude = 0
        for i in gain:
            cur += i
            max_altitude = max(max_altitude,cur) 

        return max_altitude