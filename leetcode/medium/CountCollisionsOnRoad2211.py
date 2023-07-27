class Solution:
    def countCollisions(self, directions: str) -> int:
        prev_dir = directions[0]
        collisions = 0
        num_right = 0

        for i in range(1, len(directions)):
            cur_dir = directions[i]

            if cur_dir == 'R':
                num_right += 1
                prev_dir = cur_dir
            elif cur_dir == 'S':
                if prev_dir == 'R':
                    collisions += num_right
                    num_right = 0
                    prev_dir = cur_dir
            else:       # cur_dir = 'L'
                if prev_dir == 'S':
                    collisions += 1
                if prev_dir == 'R':
                    collisions += 1 + num_right
                prev_dir = 'S'                

        print(collisions)
        return collisions
    
Solution().countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR")