class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        matches = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        for bracket in s:
            if bracket not in matches:      # opening bracket
                stack.append(bracket)
            else:                           # closing bracket
                if len(stack) == 0:
                    return False
                if matches[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
            
            
