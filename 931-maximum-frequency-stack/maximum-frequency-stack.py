class FreqStack:

    # stack of stack
    def __init__(self):
        self.freq = {}
        self.maxFreq = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        if self.freq[val] > self.maxFreq:
            self.maxFreq += 1
            self.stacks[self.maxFreq] = []
        self.stacks[self.freq[val]].append(val)

    def pop(self) -> int:
        x = self.stacks[self.maxFreq].pop()
        self.freq[x] -= 1
        if not self.stacks[self.maxFreq]:
            self.stacks.pop(self.maxFreq)
            self.maxFreq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()