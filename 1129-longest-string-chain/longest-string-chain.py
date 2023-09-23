class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # use hint, memoization
        # formula, len = max(1, len(pre) + 1)

        # l = avg len word
        # TC: O(n * l * l, O(n*logn))
        # SC: O(n)

        words.sort(key=lambda w: len(w), reverse=True)  # optimization
        words_set = set(words)
        cache = dict()  # longest chain for every word

        def dfs(word):      # will find chain length n times
            if word in cache:
                return cache[word]
            chain_size = 1
            for i in range(len(word)):      # runs size of word times, l
                pred = word[:i] + word[i + 1:]      # l 
                if pred in words_set:       # if pred exists
                    chain_size = max(chain_size, dfs(pred) + 1)
                # print(word, predecessor)
            cache[word] = chain_size       # no pred => chain_size = 1
            return chain_size

        for word in words:
            dfs(word)

        # print(cache)
        return max(cache.values())
