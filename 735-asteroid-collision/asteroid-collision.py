class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] == abs(asteroid):
                        asteroid = 0
                        stack.pop()
                        break
                    elif stack[-1] < abs(asteroid):
                        stack.pop()
                    else:
                        asteroid = 0
                        break
                if asteroid != 0:
                    stack.append(asteroid)
            # print(stack)
        return stack