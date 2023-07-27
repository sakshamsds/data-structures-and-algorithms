from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:
            # collision conditions
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = stack[-1] + asteroid
                if diff > 0:
                    asteroid = 0
                elif diff < 0:
                    stack.pop()
                else:
                    asteroid = 0
                    stack.pop()

            if asteroid:
                stack.append(asteroid)
        
        return stack



    #     stack = []

    #     for asteroid in asteroids:
    #         # print(stack)
    #         if len(stack) == 0 or stack[-1] < 0 or asteroid > 0:
    #             stack.append(asteroid)
    #         else:
    #             self.handle_collisions(stack, asteroid)
    #     # stack.reverse()
    #     return stack
    
    # def handle_collisions(self, stack, asteroid):
    #     # asteroid < 0 and stack[-1] > 0
    #     while len(stack) != 0 and asteroid < 0:
    #         top = stack[-1]
    #         if top > 0:
    #             res = top + asteroid
    #             if res < 0:
    #                 stack.pop()
    #             elif res == 0:
    #                 stack.pop()
    #                 break
    #             else:
    #                 break
    #         else:
    #             stack.append(asteroid)
    #             break

    #     if len(stack) == 0 and top < -asteroid:
    #         stack.append(asteroid)
    #     return
    
print(Solution().asteroidCollision([5,10,-5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
print(Solution().asteroidCollision([-2,-2,1,-2]))
print(Solution().asteroidCollision([-2,-2,1,-1]))
print(Solution().asteroidCollision([1, -2, -2, -2]))


            