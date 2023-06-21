# https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses
# '(', ')', '{', '}', '[' and ']'

class Solution:
    def isValid(self, s: str) -> bool:

        # neetcode solution

        stack = []
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
    
        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
        return not stack

        # stack = []
        # for char in s:
        #     if len(stack) == 0:
        #         stack.append(char)
        #     else:
        #         peek = stack[-1]
        #         if peek == "{" and char == "}":
        #             stack.pop()
        #         elif peek == "[" and char == "]":
        #             stack.pop()
        #         elif peek == "(" and char == ")":
        #             stack.pop()
        #         else:
        #             stack.append(char)

        # return len(stack) == 0