class Solution:
    def isThree(self, n: int) -> bool:
        div = set()
        for i in range(1, floor(sqrt(n)) + 1):
            # print(i)
            if n % i == 0:
                div.add(i)
                div.add(n // i)

            if len(div) > 3:
                return False

        return len(div) == 3