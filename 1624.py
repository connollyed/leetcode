class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        last_seen = {}
        max_diff = -1
        for idx,val in enumerate(s):
            if val not in last_seen:
                last_seen[val] = idx
            else:
                max_diff = max(max_diff, idx - last_seen[val] - 1)

        return max_diff