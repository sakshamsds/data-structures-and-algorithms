class Solution:
    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        q = deque([id])
        visited = set([id])
        curLevel = 1
        while q and curLevel <= level:
            for _ in range(len(q)):
                cur = q.popleft()
                for nbr in friends[cur]:
                    if nbr not in visited:
                        q.append(nbr)
                        visited.add(nbr)
            curLevel += 1

        # print(q)
        videoFreqs = collections.defaultdict(int)
        for nbr in q:
            for video in watchedVideos[nbr]:
                videoFreqs[video] += 1

        sortedVideos = [(freq, video) for video, freq in videoFreqs.items()]
        sortedVideos.sort(key=lambda x: (x[0], x[1]))
        return [video for _, video in sortedVideos]