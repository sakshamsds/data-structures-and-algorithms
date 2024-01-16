import random

class RandomizedSet:

    def __init__(self):
        self.map = dict()   # val -> idx mapping
        self.values = list()
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        # add
        self.map[val] = self.size
        self.size += 1
        self.values.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        # use pop for O(1)
        last_element = self.values[-1]
        idx = self.map[val]
        self.values[idx] = last_element
        self.map[last_element] = idx

        # remove 
        self.values.pop()
        self.map.pop(val)
        self.size -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()