class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def _insert(self, curNode, start, end):
        if curNode.end <= start:  # move the pointer right
            if not curNode.right:
                curNode.right = TreeNode(start, end)
                return True
            return self._insert(curNode.right, start, end)
        elif end <= curNode.start:
            if not curNode.left:
                curNode.left = TreeNode(start, end)
                return True
            return self._insert(curNode.left, start, end)
        else:       # overlap
            return False

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = TreeNode(startTime, endTime)
            return True
        return self._insert(self.root, startTime, endTime)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)