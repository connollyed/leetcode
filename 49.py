# O(nlogn) for sort
# Must do that M times for number of strings
# O(m*nlogn) 
#
# Space Complexity
# O(m) for number of strings and O(k) for len of strings
# O(m*k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        anagram = {}
        
        for s in strs:
            sorted_s = "".join(sorted(s))

            val = []
            if sorted_s in anagram:
                val = anagram[sorted_s]
            anagram[sorted_s] = val + [s]

        
        #print(anagram.values())
        return anagram.values()
