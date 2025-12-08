'''
    R   L   R   S   L   L

'''

class Solution:
    def countCollisions(self, directions: str) -> int:
        
        can_collide = False
        collisions = 0
        
        for d in directions[::-1]:
            if d == "L" or d == "S":
                can_collide = True

            if d == "R" and can_collide:
                collisions += 1

        can_collide = False

        for d in directions:
            if d == "R" or d == "S":
                can_collide = True

            if d == "L" and can_collide:
                collisions += 1

        return collisions
