class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-*/'
        for token in tokens:
            if token in operators:
                num2, num1 = stack.pop(), stack.pop()
                stack.append(self.operation(num1, num2, token))
            else:
                stack.append(int(token))
            # print(stack)
        return stack[0]

    def operation(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        if op == '-':
            return num1 - num2
        if op == '*':
            return num1 * num2
        if op == '/':
            return int(num1 / num2)