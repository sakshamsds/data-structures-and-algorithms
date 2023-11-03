'''
last_added = 2, num = 5
3, 4
diff - 1 = 2

'''

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        last_added = 0

        for num in target:
            for _ in range(num - last_added - 1):
                res.append("Push")
                res.append("Pop")
            res.append("Push")
            last_added = num

        return res