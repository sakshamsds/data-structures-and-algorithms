class BrowserHistory:
    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1

    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len - 1)
        return self.history[self.i]

# class ListNode:
#     def __init__(self, prev, val, next):
#         self.prev = prev
#         self.val = val
#         self.next = next

# class BrowserHistory:
#     def __init__(self, homepage: str):
#         self.current = ListNode(None, homepage, None)

#     def visit(self, url: str) -> None:
#         self.current.next = ListNode(self.current, url, None)
#         self.current = self.current.next

#     def back(self, steps: int) -> str:
#         while self.current.prev and steps>0:
#             self.current = self.current.prev
#             steps-=1
#         return self.current.val

#     def forward(self, steps: int) -> str:
#         while self.current.next and steps>0:
#             self.current = self.current.next
#             steps-=1
#         return self.current.val

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.backward_stack = []
#         self.forward_stack = []
#         self.backward_stack.append(homepage)

#     def visit(self, url: str) -> None:
#         self.backward_stack.append(url)
#         self.forward_stack.clear()

#     def back(self, steps: int) -> str:
#         for _ in range(steps):
#             if len(self.backward_stack) <= 1:
#                 break
#             self.forward_stack.append(self.backward_stack.pop())
#         return self.backward_stack[-1]

#     def forward(self, steps: int) -> str:
#         for _ in range(steps):
#             if len(self.forward_stack) <= 0:
#                 break
#             self.backward_stack.append(self.forward_stack.pop())
#         return self.backward_stack[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory("leetcode.com")
# obj.visit("google.com")
# obj.visit("facebook.com")
# obj.visit("youtube.com")
# print(obj.backward_stack, '\t-------\t' , obj.forward_stack)
# print(obj.back(1))
# print(obj.backward_stack, '\t-------\t' , obj.forward_stack)
# print(obj.back(1))
# print(obj.backward_stack, '\t-------\t' , obj.forward_stack)
# print(obj.forward(1))
# print(obj.backward_stack, '\t-------\t' , obj.forward_stack)
# obj.visit("linkedin.com")
# print(obj.backward_stack, '\t-------\t' , obj.forward_stack)
# print(obj.forward(2))
# print(obj.backward_stack, '\t-------\t' , obj.forward_stack)
# print(obj.back(2))
# print(obj.backward_stack, '\t-------\t' , obj.forward_stack)
# print(obj.back(7))
# print(obj.backward_stack, '\t-------\t' , obj.forward_stack)

