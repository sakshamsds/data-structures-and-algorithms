class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            splits = word.split(separator)
            for split in splits:
                if len(split) != 0:
                    res.append(split)

        return res