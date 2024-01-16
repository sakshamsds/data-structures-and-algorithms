class RandomizedCollection:

    def __init__(self):
        self.map = collections.defaultdict(set)   # key -> set of indices 
        self.values = list()
        self.size = 0

    def insert(self, val: int) -> bool:
        was_present = val in self.map
        self.values.append(val)
        self.map[val].add(self.size)
        self.size += 1
        return not was_present

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        idx = self.map[val].pop()       # get the last value from set
        last_element = self.values[-1]
        self.values[idx] = last_element
        self.map[last_element].add(idx)
        self.map[last_element].remove(self.size - 1)
        self.values.pop()

        if len(self.map[val]) == 0:
            self.map.pop(val)

        self.size -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()