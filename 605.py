class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0

        i = 0
        prev = 0

        while i < len(flowerbed):
            
            if i == len(flowerbed)-1:
                next = 0
            else:
                next = flowerbed[i+1]

            if flowerbed[i] == 0 and prev == 0 and next == 0:
                count += 1
                flowerbed[i] = 1

            prev = flowerbed[i]

            i += 1

        return count >= n
    

    # Improvements are add a 0 to start and end of flowerbed
    # makes the logic easier

    # After we increment count check whether count == n
    # we have sufficent condition and can exit early