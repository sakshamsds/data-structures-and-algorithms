class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):     # list of linkedlist
        self.buckets = [Node(-1, -1) for _ in range(1000)]

    def get_hash(self, key: int):
        return key % 1000

    def put(self, key: int, value: int) -> None:    # store key value pairs
        bucket_num = self.get_hash(key)
        cur = self.buckets[bucket_num]
        prev = None
        while cur:
            if cur.key == key:
                cur.val = value
                return
            prev = cur
            cur = cur.next
        prev.next = Node(key, value)

    def get(self, key: int) -> int:
        bucket_num = self.get_hash(key)
        cur = self.buckets[bucket_num]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        bucket_num = self.get_hash(key)
        cur = self.buckets[bucket_num]
        prev = None
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