class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = {'(', '[', '{'}
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for bracket in s:
            if bracket in opening_brackets:     # opening bracket
                stack.append(bracket)
            else:                               # closing bracket
                if len(stack) == 0:             # '}[]'
                    return False
                else:
                    if stack[-1] == matching[bracket]:    # matches
                        stack.pop()
                    else:
                        return False

        return len(stack) == 0