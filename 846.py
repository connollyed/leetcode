class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        n = len(hand)
        if n % groupSize != 0:
            return False

        hand.sort()
        freq = Counter(hand)

        for card in hand:
            if freq[card] > 0:
                count = freq[card]

                for i in range(groupSize):
                    if freq[card + i] < count:
                        return False
                    freq[card + i] -= count
        
        return True