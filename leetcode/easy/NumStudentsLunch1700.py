from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while len(sandwiches) != 0:
            found = False                        # iterate till match found or return
            for _ in range(len(students)):
                if students[0] == sandwiches[0]:                # case 1: match found, remove student, remove sandwich
                    students.pop(0)
                    sandwiches.pop(0)
                    found = True
                    break
                else:                                    # case 2: match not found, move student to the back
                    students.append(students.pop(0))
            if not found:
                return len(sandwiches)
        return 0