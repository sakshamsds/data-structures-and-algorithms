class Solution:
    def maxDepth(self, s: str) -> int:
        mx_depth = 0
        res = 0
        for char in s:
            if char == '(':
                res += 1
            elif char == ')':
                res -= 1
            mx_depth = max(mx_depth, res)
        return mx_depth
