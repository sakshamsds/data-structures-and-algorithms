class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                curS = []
                while stack[-1] != '[':
                    curS.append(stack.pop())
                curS = ''.join(curS[::-1])
                stack.pop()

                num = []
                while stack and '0' <= stack[-1] <= '9':
                    num.append(stack.pop())
                num = int(''.join(num[::-1]))
                stack.append(curS * num)

        return ''.join(stack)