class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr)
        if 0 in cnt and cnt[0] > 1:
            return True
        cnt.pop(0, 0)

        for num in cnt.keys():
            if 2 * num in cnt:
                return True
        return False