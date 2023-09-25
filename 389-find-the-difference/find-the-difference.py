class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        store = collections.defaultdict(int)

        for i in range(len(s)):
            store[s[i]] -= 1
            store[t[i]] += 1
        store[t[-1]] += 1
        # print(store)

        for k, v in store.items():
            if v == 1:
                return k

        return ""