'''
    left -> least recent used to more -> right

    left <=> ................................ <=> right
            hashmap (key -> Node(key, val))
'''

class ListNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.prev = left
        self.next = right

class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
        self.capacity = capacity
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):       # to the right
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self._remove(self.store[key])
        
        self.store[key] = ListNode(key, value)
        self._add(self.store[key])
        if len(self.store) > self.capacity:
            self.store.pop(self.left.next.key)
            self._remove(self.left.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)