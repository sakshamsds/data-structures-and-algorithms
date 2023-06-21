# https://leetcode.com/problems/design-hashmap/
# 706. Design HashMap

class MyHashMap:

    def __init__(self):
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):        # key is int
        return key % self.MAX

    def put(self, key: int, value: int) -> None:
        hash = self.get_hash(key)

        found = False
        for idx, (k, _) in enumerate(self.arr[hash]):
            if k == key:
                self.arr[hash][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[hash].append((key, value))

    def get(self, key: int) -> int:
        hash = self.get_hash(key)
        for k, v in self.arr[hash]:
            if k == key:
                return v
        return -1
        
    def remove(self, key: int) -> None:
        hash = self.get_hash(key)
        for k, v in self.arr[hash]:
            if k == key:
                self.arr[hash].remove((k, v))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.arr)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(2))
# obj.put(2, 1)
# print(obj.get(2))
