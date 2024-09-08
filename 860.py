class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        dict = {}
        dict[5] = 0
        dict[10] = 0
        dict[20] = 0

        for i in bills:
            if i == 5:
                dict[5] += 1


            elif i == 10:
                dict[10] += 1
                dict[5] -= 1
                if dict[5] < 0:

                    #print(dict)
                    return False

            else:
                dict[20] += 1
                if dict[10] > 0 and dict[5] > 0:
                    dict[10] -= 1
                    dict[5] -= 1
                elif dict[5] > 2:
                    dict[5] -= 3
                else:
                    #print(dict)
                    return False
                    

            #print(dict)

        return True