class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # use stack to main increasing order of chars
        # if char not seen in future, don't remove from the stack

        freq_map = collections.Counter(s)        
        # print(freq_map)
        visited = set()     # track included elements
        stack = []

        for char in s:
            if char in visited:
                freq_map[char] -= 1
                continue

            while stack:
                if stack[-1] > char and freq_map[stack[-1]] > 0:
                    # will see in future
                    visited.remove(stack[-1])
                    stack.pop()
                else:
                    break

            stack.append(char)
            freq_map[char] -= 1
            visited.add(char)

        return ''.join(stack)