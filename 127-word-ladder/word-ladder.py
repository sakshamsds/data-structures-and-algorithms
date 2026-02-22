class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjList[pattern].append(word)

        # bfs to find the shortest path
        q = deque([beginWord])
        visited = set([beginWord])
        dist = 0
        while q:
            dist += 1
            lvl_size = len(q)
            for _ in range(lvl_size):
                word = q.popleft()
                if word == endWord:
                    return dist

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nbr in adjList[pattern]:
                        if nbr not in visited:
                            q.append(nbr)
                            visited.add(nbr)

        return 0