class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()      # map key to node

        # left = LRU, right = most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove at any index
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        # node.prev.next = node.next
        # node.next.prev = node.prev

    # insert at right
    def insert(self, node):    
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev 
        # node.next = self.right
        # node.prev = self.right.prev
        # self.right.prev.next = node
        # self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])            # remove the node
            self.insert(self.cache[key])            # add that node at the right
            return self.cache[key].val
        return -1 


    def put(self, key: int, value: int) -> None:
        if key in self.cache:               
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)          # update node
        self.insert(self.cache[key])                # insert at most recent

        # check capacity after insertion
        if len(self.cache) > self.capacity:
            # lru = self.left.next
            self.cache.pop(self.left.next.key)      # remove from hashmap
            self.remove(self.left.next)             # remove LRU
            # del self.cache['key']
        return
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)