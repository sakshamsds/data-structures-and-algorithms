class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        diff = 0
        for seat_pos, student_pos in zip(seats, students):
            diff += abs(seat_pos - student_pos)
        return diff

