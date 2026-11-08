'''
Intuition: for any i, the prefix on the left has to match
            and the target suffix needs to be sorted
            and the elements should be the same

                    1   5   6   4   6
prefix match        T   T   T   T   F

                    1   5   6   6   4
suffix sorted       F   F   T   T   T

freqs = {       are the elements same or not
    6,4 
}

Edge cases:
    size = 1

TC - O(N)
SC - O(N)
'''

class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        n = len(nums)
        prefixMatch = [True] + [False] * (n - 1)        # prefix matches on the left
        for i in range(1, n):
            if nums[i - 1] == target[i - 1]:
                prefixMatch[i] = True
            else:
                break

        suffixSorted = [False] * (n - 1) + [True]       # target suffix is sorted
        for i in range(n - 2, -1, -1):
            if target[i] >= target[i + 1]:
                suffixSorted[i] = True
            else:
                break

        # print(prefixMatch)
        # print(suffixSorted)
        
        freqs = {}
        count = 0
        for i in range(n - 1, -1, -1):
            freqs[target[i]] = freqs.get(target[i], 0) + 1
            freqs[nums[i]] = freqs.get(nums[i], 0) - 1
            if nums[i] in freqs and  freqs[nums[i]] == 0:
                freqs.pop(nums[i])
            if target[i] in freqs and freqs[target[i]] == 0:
                freqs.pop(target[i])

            # print(i, freqs)
            if prefixMatch[i] and suffixSorted[i] and not freqs:
                count += 1

            if not suffixSorted[i]:
                break

        return count
