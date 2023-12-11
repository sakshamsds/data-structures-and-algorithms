class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        threshold = len(arr) // 4 + 1
        # print(len(arr), threshold)

        count = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
                if count >= threshold:
                    return arr[i]
            else:
                count = 1

        return -1