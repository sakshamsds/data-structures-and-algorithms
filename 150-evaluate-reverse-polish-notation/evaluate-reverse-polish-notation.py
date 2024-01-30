class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda x, y : x + y,
            '-': lambda x, y : x - y,
            '*': lambda x, y : x * y,
            '/': lambda x, y : x / y
        }
        for token in tokens:
            if token in operations:
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(operations[token](num1, num2)))
            else:
                stack.append(int(token))
            # print(stack)
        return stack.pop()
