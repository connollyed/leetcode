class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in arr2:
            for j in arr1:
                if i == j:
                    res.append(i)
        
        not_in = []
        for j in arr1:
            if j not in res:
                not_in.append(j)

        not_in.sort()

        return res + not_in

# Where n is number of elements in list 1
# Where m is number of elements in list 2
# Space Complexity = O(n+m)
# Time Complexity = O(n*m) + O(nlogn)


def relativeSortArray(arr1, arr2):
    # Create a dictionary to store the index of each element in arr2
    index_map = {val: i for i, val in enumerate(arr2)}
    
    # Custom sorting function to sort arr1 based on the index in arr2
    def custom_sort(element):
        if element in index_map:
            return (0, index_map[element])
        else:
            return (1, element)
    
    # Sort arr1 using the custom sort function
    arr1.sort(key=custom_sort)
    
    return arr1


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:       
        pos = defaultdict(int)

        end = []
        for i in arr1:
            if i in arr2:
                pos[i] += 1
            else:
                end.append(i) 

        print(end)
        res = []
        for i in arr2:
            for j in range((pos[i])):
               res.append(i)


        if len(end) > 0 :
            res = res + sorted(end)
        return res