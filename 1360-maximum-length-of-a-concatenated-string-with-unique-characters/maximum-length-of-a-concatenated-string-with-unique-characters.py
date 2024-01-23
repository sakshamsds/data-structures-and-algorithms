class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = set()

        def backtrack(i):
            max_size = len(res)
            if i == len(arr):
                return max_size

            for j in range(i, len(arr)):
                if len(set(arr[j])) == len(arr[j]) and not res & set(arr[j]):
                    res.update(arr[j])
                    max_size = max(backtrack(j + 1), max_size)
                    res.difference_update(arr[j])
            return max_size

        return backtrack(0)