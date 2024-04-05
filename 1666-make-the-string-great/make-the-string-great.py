class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for cur in s:
            if not stack:
                stack.append(cur)
                continue

            prev = stack[-1]
            if prev == cur:
                stack.append(cur)
                continue
            
            if prev.lower() == cur.lower():
                stack.pop()
                continue

            stack.append(cur)

        return ''.join(stack)
