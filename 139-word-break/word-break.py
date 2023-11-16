class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom up approach
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # enough letters to compare
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:   # if already true, no need to compare more words
                    break

        # print(dp)
        return dp[0]