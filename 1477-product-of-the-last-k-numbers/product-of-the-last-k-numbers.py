class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]          # prefix pdts

    def add(self, num: int) -> None:
        if num == 0:            # if num = 0, clean the array
            self.nums = [1]
        else:
            self.nums.append(num * self.nums[-1])
        
    def getProduct(self, k: int) -> int:
        if len(self.nums) - 1 < k:
            return 0
        return self.nums[-1] // self.nums[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)