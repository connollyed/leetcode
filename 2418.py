class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(names)
        i = 0    

        dict = {}

        i = 0
        while i < n:
            dict[heights[i]] = names[i]
            i += 1


        heights.sort()

        output = []
        i=n-1
        while i >= 0:
            output.append(dict[heights[i]])
            i-=1

        return output