class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        loses = {}
        for idx,[W,L] in enumerate(matches):
            if W not in loses:
                loses[W] = 0

            if L not in loses:
                loses[L] = 1
            else:
                loses[L] += 1
        
        lose_zero = []
        lose_one = []
        for player, loses in (loses.items()):
            if loses == 0:
                lose_zero.append(player)
            elif loses == 1:
                lose_one.append(player)

        return [sorted(lose_zero), sorted(lose_one)]