class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        res = []
        stack = []
        for h in heights[::-1]:
            cnt = 0
            while stack and stack[-1] < h:
                cnt += 1
                stack.pop()

            if stack:
                cnt += 1
            
            stack.append(h)
            res.append(cnt)

        return res[::-1]
        