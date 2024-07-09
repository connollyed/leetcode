class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        freq = {
            "b":0,
            "a":0,
            "l":0,
            "o":0,
            "n":0
        }
        for i in text:
            if i in freq:

                freq[i] = freq[i] + 1

        return min(freq["b"],freq["a"],freq["l"]//2,freq["o"]//2,freq["n"])