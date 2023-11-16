class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        cache = {}
        cache[len(s)] = True

        # @cache
        def dfs(i):
            # if i == len(s):   # base case
                # return True
            # print(i)
            if i in cache:
                return cache[i]

            # at every idx try all the words to see if you get a match
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    if dfs(i + len(w)):
                        cache[i] = True
                        return True

            cache[i] = False
            return False

        return dfs(0)


        