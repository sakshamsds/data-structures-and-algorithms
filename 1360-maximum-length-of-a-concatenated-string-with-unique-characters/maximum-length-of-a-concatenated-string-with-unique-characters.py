class Solution:
    def maxLength(self, arr: List[str]) -> int:
        freqs = [0] * 26

        def dfs(i):
            if i == len(arr):
                return sum(freqs)

            # do not include
            max_len = dfs(i + 1)

            unique = True
            for c in arr[i]:
                if freqs[ord(c) - 97] > 0:
                    unique = False
                    break

            if unique and len(set(arr[i])) == len(arr[i]):            
                for c in arr[i]:
                    freqs[ord(c) - 97] += 1
                max_len = max(max_len, dfs(i + 1))
                for c in arr[i]:
                    freqs[ord(c) - 97] -= 1

            return max_len

        return dfs(0)