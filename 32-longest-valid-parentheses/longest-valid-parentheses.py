class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        longest = 0
        for i, c in enumerate(s):
            if c == '(':            # this won't be valid so no calculation
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    left = -1 if not stack else stack[-1]
                    longest = max(longest, i - left) 
                else:
                    stack.append(i)
            # print(stack)

        return longest