class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        def evaluate(num2, num1, token):
            if token == '+':
                return num1 + num2
            if token == '-':
                return num1 - num2
            if token == '*':
                return num1 * num2
            div = num1 / num2
            return math.ceil(div) if div < 0 else math.floor(div)


        for token in tokens:
            if token in ['+', '-', '*', '/']:
                evaluated = evaluate(stack.pop(), stack.pop(), token)
                # print(stack, evaluated)
                stack.append(evaluated)
            else:
                stack.append(int(token))
        
        return stack[0]

