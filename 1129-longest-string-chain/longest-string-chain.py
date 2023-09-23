class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # use hint, memoization
        # formula, len = max(1, len(pre) + 1)
        words_set = set(words)
        cache = dict()

        def dfs(word):
            if word not in words_set:
                return 0

            if word in cache:
                return cache[word]

            chain_length = 1
            for i in range(len(word)):
                # remove ith char
                predecessor = word[:i] + word[i + 1:]
                chain_length = max(chain_length, dfs(predecessor) + 1)
                # print(word, predecessor)

            cache[word] = chain_length
            return chain_length

        max_length = 1
        for word in words:
            max_length = max(max_length, dfs(word))

        # print(cache)
        return max_length
