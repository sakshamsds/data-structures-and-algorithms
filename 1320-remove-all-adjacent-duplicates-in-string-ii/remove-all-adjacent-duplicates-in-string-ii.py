class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # c, freq
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append((c, 1))
            else:
                freq = stack.pop()[1]
                if freq < k - 1:
                    stack.append((c, freq + 1))
        return ''.join([c * freq for c, freq in stack])