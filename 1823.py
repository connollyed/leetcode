class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        people = [i+1 for i in range(n)]
        kill = 0
        #print(people)
        while len(people) > 1:
            kill = (kill + k-1) % len(people)
            people.pop(kill)
            #print(people)

        return people[0]