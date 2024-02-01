class StockSpanner:

    def __init__(self):
        self.stack = [(inf, 0)]
        self.pos = 0

    def next(self, price: int) -> int:
        # print(self.stack)
        while self.stack[-1][0] <= price:     # remove lower prices
            self.stack.pop()
        self.pos += 1
        self.stack.append((price, self.pos))
        return self.pos - self.stack[-2][1] 

        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)