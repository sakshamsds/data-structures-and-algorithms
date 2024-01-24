class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for bracket in s:
            if bracket not in matches:     # opening bracket
                stack.append(bracket)
            else:                               # closing bracket
                if stack and stack[-1] == matches[bracket]:
                    stack.pop()
                else:
                    return False

        return not stack