'''
(u(love)i) = iloveu
(u(lov)ei) = (uvolei) = ielovu
(u(lov)ei) = ie(vol)u = ielovu 
'''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        # stack solution, O(n^2)

        stack = []
        for c in s:
            if c == ')':
                portion = []
                while stack[-1] != '(':
                    portion.append(stack.pop())
                stack.pop()
                stack.extend(portion)
            else:
                stack.append(c)
        return ''.join(stack)