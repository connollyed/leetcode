class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        total = 0
        for idx in range(len(seats)):
            total += abs(seats[idx] - students[idx])

        return total