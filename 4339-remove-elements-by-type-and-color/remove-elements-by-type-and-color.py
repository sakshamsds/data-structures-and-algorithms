class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        stack = []          # type, color, freq
        for i in range(len(types)):
            elementType, color = types[i], colors[i]
            size = groupSize[elementType]
            if size == 1:
                continue
            if not stack or (stack[-1][0] != elementType or stack[-1][1] != color):
                stack.append((elementType, color, 1))
            else:
                _, _, freq = stack.pop()
                if freq + 1 != size:
                    stack.append((elementType, color, freq + 1))
        return not stack