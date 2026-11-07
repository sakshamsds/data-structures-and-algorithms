class Node:
    def __init__(self, key, val, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt

class MyHashMap:

    def __init__(self):
        self.maxBuckets = 1000        
        self.map = [Node(-1, -1) for _ in range(self.maxBuckets)] 

    def getHash(self, key: int) -> int:
        return key % self.maxBuckets

    def put(self, key: int, val: int) -> None:
        h = self.getHash(key)
        prev = self.map[h]
        cur = prev.next
        while cur:
            if cur.key == key:
                cur.val = val
                return
            prev = cur
            cur = cur.next
        prev.next = Node(key, val)

    def get(self, key: int) -> int:
        h = self.getHash(key)
        cur = self.map[h]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        h = self.getHash(key)
        prev = self.map[h]
        cur = prev.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)