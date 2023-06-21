# https://leetcode.com/problems/design-hashset/
# 705. Design HashSet
# Use Chaining/Linked Lists, open addressing == Linear probing?


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.MAX = 1000
        self.arr = [ListNode(-1, None) for _ in range(self.MAX)]        # dummy node helps avoid edge cases

    def get_hash(self, key):
        return key % self.MAX

    def add(self, key: int) -> None:
        hash = self.get_hash(key)
        current = self.arr[hash]
        while current.next:
            if current.next.val == key:
                return
            current = current.next
        current.next = ListNode(key, None)
        
    def remove(self, key: int) -> None:
        hash = self.get_hash(key)
        current = self.arr[hash]
        while current.next:
            if current.next.val == key:
                current.next = current.next.next
                break
            current = current.next

    def contains(self, key: int) -> bool:
        hash = self.get_hash(key)
        current = self.arr[hash]
        while current.next:
            if current.next.val == key:
                return True
            current = current.next
        return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(1)
# obj.remove(1)
# obj.add(2)
# print(obj.contains(1))
# print(obj.contains(3))
# obj.add(2)
# print(obj.contains(2))
# obj.remove(2)