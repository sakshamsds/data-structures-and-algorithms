'''
    R   L   R   S   L   L
'''

class Solution:
    def countCollisions(self, directions: str) -> int:
        
        def get_collisions(traversal, stationary, other_dir):
            can_collide = False
            collisions = 0
            for d in directions[::traversal]:
                if d == stationary or d == "S":
                    can_collide = True

                if d == other_dir and can_collide:
                    collisions += 1
            return collisions
        
        return get_collisions(1, "R", "L") + get_collisions(-1, "L", "R") 