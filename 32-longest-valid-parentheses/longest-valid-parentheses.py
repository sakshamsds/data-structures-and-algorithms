class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []      # (, idx
        longest = 0

        for i, c in enumerate(s):
            if c == '(' or not stack or stack[-1][0] != '(':
                stack.append((c, i))
            else:
                stack.pop()
                prevI = -1 if not stack else stack[-1][1]
                longest = max(longest, i - prevI)
            # print(stack)
        return longest