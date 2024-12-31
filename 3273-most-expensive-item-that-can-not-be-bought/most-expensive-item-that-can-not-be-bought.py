class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        # Chicken McNugget Theorem
        return primeOne * primeTwo - primeOne - primeTwo