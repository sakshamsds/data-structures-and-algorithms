class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        freqs = collections.Counter(s)
        visited = set()

        for char in s:
            if char in visited:
                freqs[char] -= 1
                continue
            
            while stack:
                if stack[-1] > char and  freqs[stack[-1]] > 0:
                    visited.remove(stack[-1])
                    stack.pop()
                else:
                    break

            stack.append(char)
            visited.add(char)
            freqs[char] -= 1

        return "".join(stack)